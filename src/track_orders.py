class TrackOrders:
    def __init__(self):
        self._length = 0
        self._orders = []

    def __len__(self):
        return self._length

    def add_new_order(self, customer, order, day):
        order_info = {
            "cliente": customer,
            "pedido": order,
            "dia": day,
        }
        self._orders.append(order_info)
        self._length += 1

    def get_most_ordered_dish_per_customer(self, customer):
        order_amount = {order["pedido"]: 0 for order in self._orders}
        for order in self._orders:
            pedido = order["pedido"]
            cliente = order["cliente"]
            if cliente == customer:
                order_amount[pedido] += 1
        max_amount = max(order_amount.values())
        return [key for key,
                value in order_amount.items() if value == max_amount][0]

    def get_never_ordered_per_customer(self, customer):
        order_amount = {order["pedido"]: 0 for order in self._orders}
        for order in self._orders:
            pedido = order["pedido"]
            cliente = order["cliente"]
            if cliente == customer:
                order_amount[pedido] += 1
        return {key for key,
                value in order_amount.items() if value == 0}

    def get_days_never_visited_per_customer(self, customer):
        order_days = {order["dia"]: 0 for order in self._orders}
        for order in self._orders:
            dia = order["dia"]
            cliente = order["cliente"]
            if cliente == customer:
                order_days[dia] += 1
        return {key for key,
                value in order_days.items() if value == 0}

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
