import json


def load_data(path: str = '../data/operations.json'):
    """
    получает файл джейсон
    :return: возвращает список со словарями
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# print(type(load_data('../data/operations.json')))