#! /usr/bin/python3

import os
from enum import Enum
import sys

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
    def __init__(self, id_, title='', title_slug='', difficulty=0):
        self.id_ = id_
        self.title = title
        self.title_slug = title_slug
        self.difficulty = difficulty
        # key is Language enum, value is file name
        self.solution = {}

    def difficulty_str(self):
        switcher = {
            1: 'Easy',
            2: 'Medium',
            3: 'Hard',
        }
        return switcher.get(self.difficulty, "")

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Handler:
    def __init__(self, path):
        self.path = path
        self.done_questions = {}
        self.remote_questions = {}
        self.summary = {}
        for language in Language:
            self.summary[language] = [0] * 4

    def fetch_remote_questions(self):
        qs = requests.get('https://leetcode.com/api/problems/algorithms/').json()['stat_status_pairs']
        for q in qs:
            stat = q['stat']
            question = Question(stat['frontend_question_id'], stat['question__title'], stat['question__title_slug'],
                                q['difficulty']['level'])
            self.remote_questions[question.id_] = question

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
            rq = self.remote_questions[q.id_]
            q.title = rq.title
            q.title_slug = rq.title_slug
            q.difficulty = rq.difficulty
            for lang in q.solution:
                self.summary[lang][q.difficulty] += 1
                self.summary[lang][0] += 1

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
        for i in [1, 2, 3, 0]:
            difficulty = Question(0, difficulty=i).difficulty_str()
            if not difficulty:
                difficulty = "Total"
            sb.append(
                f'|{difficulty}|{summary[Language.GO][i]}|{summary[Language.PYTHON][i]}|{summary[Language.RUST][i]}|')

        sb.extend(['\n### Problems', '| # | Title | Solution | Difficulty |', '|:---:' * 4 + '|'])
        for q in questions:
            solution = []
            languages = list(q.solution.keys())
            languages.sort(key=lambda x: x.value)
            id_dir = os.path.join(self.path, '{:04d}'.format(q.id_))
            for k in languages:
                solution.append(f'[{k}]({os.path.join(id_dir, q.solution[k])})')
            data = {
                'id': f'[{q.id_}]({id_dir})',
                'title': f'[{q.title}](https://leetcode.com/problems/{q.title_slug}/)',
                'solution': ('&nbsp;' * 2).join(solution),
                'difficulty': q.difficulty_str(),
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
