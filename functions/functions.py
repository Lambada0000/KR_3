import json


def get_json_file() -> list[dict, ...]:
    """
    Функция считывает файл Json
    и возвращает список словарей
    """
    with open("operations/operations.json") as file:
        file = json.load(file)
        return file