from os.path import exists
import csv


def maria_orders(orders):
    total_orders = {order["pedido"]: 0 for order in orders}
    for order in orders:
        cliente = order["cliente"]
        pedido = order["pedido"]
        if cliente == "maria":
            total_orders[pedido] += 1
    return total_orders


def arnaldo_orders(orders):
    total_orders = {order["pedido"]: 0 for order in orders}
    for order in orders:
        cliente = order["cliente"]
        pedido = order["pedido"]
        if cliente == "arnaldo":
            total_orders[pedido] += 1
    return total_orders


def joao_orders(orders):
    total_orders = {order["pedido"]: 0 for order in orders}
    for order in orders:
        cliente = order["cliente"]
        pedido = order["pedido"]
        if cliente == "joao":
            total_orders[pedido] += 1
    return total_orders


def joao_days(orders):
    total_days = {order["dia"]: 0 for order in orders}
    for order in orders:
        cliente = order["cliente"]
        dia = order["dia"]
        if cliente == "joao":
            total_days[dia] += 1
    return total_days


def write_data(file_name, data):
    with open(file_name, mode="w", encoding="UTF-8") as file:
        for entry in data:
            file.write(str(entry))
            file.write("\n")


def analyze_log(path_to_file):
    if not exists(path_to_file):
        raise(FileNotFoundError("Arquivo inexistente: '{path_to_file}'"))

    result = []

    with open(path_to_file, encoding="UTF-8") as file:
        table = csv.DictReader(file, delimiter=",",
                               fieldnames=["cliente", "pedido", "dia"])
        data = [row for row in table]

    maria = maria_orders(data)
    most_ordered = max(maria.values())
    result.append(
        [key for key, value in maria.items() if value == most_ordered][0])

    arnaldo = arnaldo_orders(data)
    result.append(arnaldo["hamburguer"])

    joao = joao_orders(data)
    never_ordered = {key for key, value in joao.items() if value == 0}
    result.append(never_ordered)

    joao_went_to_snack_bar = joao_days(data)
    never_went_to_snack_bar = {
        key for key, value in joao_went_to_snack_bar.items() if value == 0}
    result.append(never_went_to_snack_bar)

    write_data("data/mkt_campaign.txt", result)
