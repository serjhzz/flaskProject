import json


def load_candidates() -> list:
    """
    Функция загрузки данных из файла.
    :return: Список всех кандидатов прочитанных из файла.
    """
    file_candidates = 'candidates.json'
    with open(file_candidates, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_all(data: list) -> list:
    """
    Функция получения всего списка кандидатов.
    :param data: Список прочитанный из файла.
    :return: Список кандидатов.
    """
    return data


def get_by_pk(data: list, pk: int) -> list:
    """
    Функция получения кандидата по pk.
    :param data: Список прочитанный из файла.
    :param pk: pk кандидата.
    :return: Информация о кандидате в виде списка его параметров.
    """
    return data[pk - 1]


def get_by_skill(data: list, skill_name: str) -> list:
    """
    Функция получения кандидатов по навыку.
    :param data: Список прочитанный из файла.
    :param skill_name: Название навыка.
    :return: Список кандидатов с выбранным навыком.
    """
    skill_list = []
    for d in data:
        if skill_name in d['skills'].lower():
            skill_list.append(d)
    return skill_list
