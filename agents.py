class Agent:
    def __init__(self, idx, *items):
        self.id = idx
        self.items = {i[0]: 0 for i in items}
        self.values = {i[0]: i[1] for i in items}
        self.capacities = {i[0]: i[2] for i in items}

    def check_item(self, item_id, price):
        return self.check_price(item_id, price) and self.check_capacity(item_id)

    def check_price(self, item_id, price):
        return self.values[item_id] >= price

    def check_capacity(self, item_id):
        return self.capacities[item_id] > self.items[item_id]

    def add_item(self, item_id):
        self.items[item_id] += 1

    def remove_item(self, item_id):
        if self.items[item_id] == 0:
            raise Warning('Negative amount of items is attempted to be assigned')
        self.items[item_id] -= 1

    def modify_values(self, modifier):
        self.values = {k: max(v + modifier, 0) for k, v in self.values.items()}
        return self

    def modify_capacities(self, modifier):
        self.capacities = {k: max(v + modifier, 1) for k, v in self.capacities.items()}
        return self
