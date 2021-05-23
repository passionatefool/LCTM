#! /usr/bin/python3

import json
import os
import sys

import requests

PYTHON = 'Python'
GO = 'Go'
RUST = 'Rust'


class Question:
    def __init__(self, id_):
        self.id_ = id_
        self.title = ''
        self.title_slug = ''
        self.difficulty = 0
        self.solution = {}

    def difficulty_str(self):
        switcher = {
            1: 'Easy',
            2: 'Medium',
            3: 'Hard',
        }
        return switcher.get(self.difficulty, "None")

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Handler:
    def __init__(self, path):
        self.path = path
        self.done_questions = {}
        self.remote_questions = {}
        self.summary = {}
        for language in [GO, PYTHON, RUST]:
            self.summary[language] = [0] * 4

    def fetch_remote_questions(self):
        content = requests.get('https://leetcode.com/api/problems/algorithms/').content
        qs = json.loads(content)['stat_status_pairs']
        for q in qs:
            stat = q['stat']
            question = Question(stat['frontend_question_id'])
            question.title = stat['question__title']
            question.title_slug = stat['question__title_slug']
            question.difficulty = q['difficulty']['level']
            self.remote_questions[question.id_] = question

    def parse_done_questions(self):
        for path, dir_list, file_list in os.walk(self.path):
            for file_name in file_list:
                base_path = os.path.basename(path)
                if file_name.endswith('.py'):
                    q = self.get_or_set_done_question(int(base_path))
                    q.solution[PYTHON] = file_name
                elif file_name.endswith('.go'):
                    q = self.get_or_set_done_question(int(base_path))
                    q.solution[GO] = file_name
                elif file_name.endswith('.rs'):
                    q = self.get_or_set_done_question(int(base_path))
                    q.solution[RUST] = file_name

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
        sb = [
            '# LCTM\n',
            '### Summary',
            '||{}|{}|{}|'.format(GO, PYTHON, RUST), '|:---:' * 4 + '|',
            '|Easy|{}|{}|{}|'.format(self.summary[GO][1], self.summary[PYTHON][1], self.summary[RUST][1]),
            '|Medium|{}|{}|{}|'.format(self.summary[GO][2], self.summary[PYTHON][2], self.summary[RUST][2]),
            '|Hard|{}|{}|{}|'.format(self.summary[GO][3], self.summary[PYTHON][3], self.summary[RUST][3]),
            '|Total|{}|{}|{}|\n'.format(self.summary[GO][0], self.summary[PYTHON][0], self.summary[RUST][0]),
            '### Problems', '| # | Title | Solution | Difficulty |', '|:---:' * 4 + '|',
        ]

        for q in questions:
            solution = []
            languages = list(q.solution.keys())
            languages.sort()
            id_dir = os.path.join(self.path, '{:04d}'.format(q.id_))
            for k in languages:
                solution.append('[{}]({})'.format(k, os.path.join(id_dir, q.solution[k])))
            data = {
                'id': '[{}]({})'.format(q.id_, id_dir),
                'title': '[{}](https://leetcode.com/problems/{}/)'.format(q.title, q.title_slug),
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
