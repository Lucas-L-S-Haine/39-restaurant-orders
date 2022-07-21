class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._customer_orders = []
        self._needed_ingredients = {ingredient: 0 for ingredient
                                    in self.MINIMUM_INVENTORY.keys()}

    def add_new_order(self, customer, order, day):
        customer_order = {
            "cliente": customer,
            "pedido": order,
            "dia": day,
        }
        for ingredient in self.INGREDIENTS[order]:
            self._needed_ingredients[ingredient] += 1
            if (self._needed_ingredients[ingredient]
                    > self.MINIMUM_INVENTORY[ingredient]):
                return False
        self._customer_orders.append(customer_order)
        return customer_order

    def get_quantities_to_buy(self):
        return self._needed_ingredients

    def get_available_dishes(self):
        dishes = {"hamburguer", "pizza", "misto-quente", "coxinha"}
        unavailable_dishes = set()
        available_ingredients = self.MINIMUM_INVENTORY.copy()
        for ing in available_ingredients.keys():
            available_ingredients[ing] -= self._needed_ingredients[ing]
        for dish in dishes:
            for ingredient in self.INGREDIENTS[dish]:
                if available_ingredients[ingredient] <= 0:
                    unavailable_dishes.add(dish)
        return dishes - unavailable_dishes
