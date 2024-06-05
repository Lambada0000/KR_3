import json
from operator import itemgetter


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

    completed_operations = []
    for operation in list_:
        if operation.get("state") == "EXECUTED":
            completed_operations.append(operation)
    return completed_operations


def get_latest_transactions(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Функция принимает список словарей и отсортировывает их по дате, возвращая
    только пять последних операций по дате
    :param list_: список словарей
    :return: пять первых элементов в списке
    """

    # Сортируем список словарей по ключу "date" в порядке убывания
    sorted_list = sorted(list_, key=itemgetter("date"), reverse=True)

    # Добавляем первые пять элементов из отсортированного списка в новый список
    latest_transactions = []
    for i in range(min(5, len(sorted_list))):
        latest_transactions.append(sorted_list[i])

    return latest_transactions


def get_date_from_string(list_: list[dict, ...]) -> tuple[str, ...]:
    """
    Функция принимает список словарей и возвращает кортеж из дат и типов операций.
    :param list_: список словарей
    :return: кортеж строк
    """

    dates = []
    descriptions = []
    for transaction in list_:
        # Извлекаем дату и берем первые 10 символов, заменяя дефисы на точки
        date = transaction["date"][:10].replace("-", ".")
        dates.append(date)
        description = transaction["description"]
        descriptions.append(description)

    # Создаем список для хранения дат в формате DD.MM.YYYY
    reversed_dates = []
    for date in dates:
        # Разбиваем дату на части (YYYY, MM, DD), переворачиваем и соединяем обратно
        parts = date.split(".")
        reversed_date = ".".join(parts[::-1])
        reversed_dates.append(reversed_date)

    result = []
    for i in range(len(reversed_dates)):
        final_string = reversed_dates[i] + " " + descriptions[i]
        result.append(final_string)

    return tuple(result)


