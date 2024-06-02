import json


def get_json_file() -> list[dict, ...]:
    """
    Функция считывает файл Json
    :return: список словарей
    """
    with open("operations/operations.json") as file:
        file = json.load(file)
        return file


def get_list_completed_operations(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Функция принимает список словарей и сортирует его по выполненным операциям
    :param list_: список словарей
    :return: список словарей
    """
    completed_operations = [operation for operation in list_ if operation.get("state") == "EXECUTED"]
    return completed_operations


def get_latest_transactions(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Функция принимает список словарей и отсортировывает их по дате возвращая
    только пять последних операций по дате
    :param list_: список словарей
    :return: пять первых элементов в списке
    """
    latest_transactions = sorted(list_, key=lambda date: date["date"], reverse=True)
    return latest_transactions[:5]