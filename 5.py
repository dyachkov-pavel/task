import os
import re


def task1():
    # в папке test найти все файлы filenames вывести колличество
    def count_files(dir_path):
        num = 0
        for element in os.listdir(dir_path):
            element_path = os.path.join(dir_path, element)
            if os.path.isfile(element_path):
                if 'filenames' in element:
                    num += 1
            elif os.path.isdir(element_path):
                num += count_files(element_path)
        return num

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return count_files(os.path.join(base_dir, 'task', 'test'))


def task2():
    # в папке test найти все email адреса записанные в файлы
    emails = []
    regexp = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def find_emails(dir_path):
        for element in os.listdir(dir_path):
            element_path = os.path.join(dir_path, element)
            if os.path.isfile(element_path):
                with open(element_path, 'r') as file:
                    for line in file:
                        found_emails = re.findall(regexp, line)
                        if not found_emails:
                            continue
                        for email in found_emails:
                            emails.append(email)
            elif os.path.isdir(element_path):
                find_emails(element_path)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    find_emails(os.path.join(base_dir, 'task', 'test'))
    return emails


def main():
    print(task1())
    print(task2())
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
