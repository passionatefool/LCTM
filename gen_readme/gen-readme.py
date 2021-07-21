#! /usr/bin/python3

import os
from enum import Enum
import sys
import json

import requests


class Language(Enum):
    PYTHON = 'Python'
    GO = 'Go'
    RUST = 'Rust'

    def suffix(self) -> str:
        r = ""
        if self == self.__class__.PYTHON:
            r = '.py'
        elif self == self.__class__.GO:
            r = '.go'
        elif self == self.__class__.RUST:
            r = '.rs'
        return r

    def __str__(self):
        return self.value


class Question:
    def __init__(self, id_, title='', title_slug='', difficulty=''):
        self.id_ = id_
        self.title = title
        self.title_cn = ''
        self.title_slug = title_slug
        self.difficulty = difficulty
        # key is Language enum, value is file name
        self.solution = {}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Handler:
    def __init__(self, path):
        self.path = path
        self.done_questions = {}
        self.remote_questions = {}
        self.summary = {}
        for language in Language:
            self.summary[language] = {'EASY':0,'MEDIUM':0,'HARD':0,'TOTAL':0}

    def fetch_remote_questions(self):
        cache_file_path='./cache/questions.json'
        if os.path.isfile(cache_file_path):
            with open(cache_file_path,'r',encoding='utf8')as f:
                json_data=json.load(f)
                for key in json_data:
                    q=Question(0)
                    q.__dict__.update(json_data[key])
                    self.remote_questions[key]=q
                return
        for i in range (30):
            qs_cn = requests.post('https://leetcode-cn.com/graphql/',data=self.get_raw_data(i*100,100*(i+1)),headers={'content-type': 'application/json'}).json()['data']['problemsetQuestionList']['questions']
            if len(qs_cn)==0:
                break
            for q in qs_cn:
                question = Question(str(q['frontendQuestionId']),q['title'],q['titleSlug'],
                                q['difficulty'])
                question.title_cn=q['titleCn']
                self.remote_questions[question.id_] = question
        with open(cache_file_path, 'w', encoding='utf-8') as f:
            json.dump(self.remote_questions,f,default=lambda obj:obj.__dict__,  ensure_ascii=False, indent=4)



    def parse_done_questions(self):
        for path, dir_list, file_list in os.walk(self.path):
            for file_name in file_list:
                base_path = os.path.basename(path)
                if not base_path.isdigit():
                    continue
                id_ = int(base_path)
                if file_name.endswith(Language.PYTHON.suffix()):
                    q = self.get_or_set_done_question(id_)
                    q.solution[Language.PYTHON] = file_name
                elif file_name.endswith(Language.GO.suffix()):
                    q = self.get_or_set_done_question(id_)
                    q.solution[Language.GO] = file_name
                elif file_name.endswith(Language.RUST.suffix()):
                    q = self.get_or_set_done_question(id_)
                    q.solution[Language.RUST] = file_name

    def merge_questions(self):
        for q in self.done_questions.values():
            rq = self.remote_questions[str(q.id_)]
            q.title = rq.title
            q.title_cn = rq.title_cn
            q.title_slug = rq.title_slug
            q.difficulty = rq.difficulty
            for lang in q.solution:
                self.summary[lang][q.difficulty] += 1
                self.summary[lang]['TOTAL'] += 1

    def get_raw_data(self,skip,limit):
        return r'{"query":"\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    hasMore\n    total\n    questions {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId\n      isFavor\n      paidOnly\n      solutionNum\n      status\n      title\n      titleCn\n      titleSlug\n      topicTags {\n        name\n        nameTranslated\n        id\n        slug\n      }\n      extra {\n        hasVideoSolution\n        topCompanyTags {\n          imgUrl\n          slug\n          numSubscribed\n        }\n      }\n    }\n  }\n}\n    ","variables":{"categorySlug":"","skip":'+str(skip)+r',"limit":'+str(limit)+r',"filters":{}},"operationName":"problemsetQuestionList"}'

    def get_or_set_done_question(self, id_):
        if id_ in self.done_questions:
            return self.done_questions[id_]
        question = Question(id_)
        self.done_questions[id_] = question
        return question

    def render(self) -> str:
        questions = list(self.done_questions.values())
        questions.sort(key=lambda x: x.id_)
        summary = self.summary
        sb = [
            '# LCTM\n',
            '### Summary',
            f'||{Language.GO}|{Language.PYTHON}|{Language.RUST}|',
            '|:---:' * 4 + '|',
        ]
        for i in ['EASY', 'MEDIUM', 'HARD', 'TOTAL']:
            sb.append(
                f'|{i}|{summary[Language.GO][i]}|{summary[Language.PYTHON][i]}|{summary[Language.RUST][i]}|')

        sb.extend(['\n### Problems', '| # | Title | Solutions | Difficulty |', '|:---:' * 4 + '|'])
        for q in questions:
            solution = []
            languages = list(q.solution.keys())
            languages.sort(key=lambda x: x.value)
            id_dir = os.path.join(self.path, '{:04d}'.format(q.id_))
            for k in languages:
                solution.append(f'[{k}]({os.path.join(id_dir, q.solution[k])})')
            data = {
                'id': f'[{q.id_}]({id_dir})',
                'title': f'[{q.title}](https://leetcode.com/problems/{q.title_slug}/)&nbsp;&nbsp;[{q.title_cn}](https://leetcode-cn.com/problems/{q.title_slug}/)',
                'solution': ('&nbsp;' * 2).join(solution),
                'difficulty': q.difficulty,
            }
            sb.append('|{id}|{title}|{solution}|{difficulty}|'.format(**data))
        return '\n'.join(sb)


def main():
    h = Handler(sys.argv[1])
    h.fetch_remote_questions()
    h.parse_done_questions()
    h.merge_questions()
    print(h.render())


if __name__ == '__main__':
    main()
