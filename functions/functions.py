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


def get_date_from_string(list_: list[dict, ...]) -> tuple[str, ...]:
    """
    Функция принимает список словарей и возвращает кортеж из дат и типов операций
    :param list_: список словарей
    :return: кортеж строк
    """
    date = [data["date"][:10].replace("-", ".") for data in list_]
    list_operations = [description["description"] for description in list_]
    revers_data = [".".join(data.split(".")[::-1]) for data in date]
    type_transaction = (f"{revers_data[0] + " " + list_operations[0]}",
                        f"{revers_data[1] + " " + list_operations[1]}",
                        f"{revers_data[2] + " " + list_operations[2]}",
                        f"{revers_data[3] + " " + list_operations[3]}",
                        f"{revers_data[4] + " " + list_operations[4]}")

    return type_transaction

