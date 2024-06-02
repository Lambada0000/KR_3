from functions.functions import *


def main() -> str:
    list_banking_transactions = get_json_file()
    list_completed_operations = get_list_completed_operations(list_banking_transactions)
    last_five_operations = get_latest_transactions(list_completed_operations)