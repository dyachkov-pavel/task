import argparse
import json
import sys


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',)
    return parser


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count = 0
    rounds = data['game']['rounds']
    for round in rounds:
        count += len(round['questions'])
    print(f'Количество вопросов: {count}')


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    rounds = data['game']['rounds']
    for round in rounds:
        questions = round['questions']
        for question in questions:
            correct_answers.append(question['correct_answer'])
    print('Правильные ответы:', correct_answers)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_settings_time = 0  # time_to_answer в settings
    max_answer_time = 0  # time_to_answer в questions
    rounds = data['game']['rounds']
    for round in rounds:
        round_settings = round.get('settings')
        if not round_settings:
            continue
        time = round_settings['time_to_answer']
        if time > max_settings_time:
            max_settings_time = time
        questions = round['questions']
        for question in questions:
            time_to_answer = question.get('time_to_answer')
            if not time_to_answer:
                continue
            if time_to_answer > max_answer_time:
                max_answer_time = question['time_to_answer']
    print('Макс. время ответа:', max(max_settings_time, max_answer_time))


def main(file_name):
    # загрузить данные из test.json файла
    try:
        with open(file_name) as json_file:
            data = json.load(json_file)
            count_questions(data)
            print_right_answers(data)
            print_max_answer_time(data)
    except OSError as e:
        print(e)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    # python 4.py -f test.json / python 4.py --file test.json
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.file and namespace.file.endswith('.json'):
        main(namespace.file)
    else:
        print('Введите имя файла с расширением json')
