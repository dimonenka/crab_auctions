class Item:
    def __init__(self, idx, reserve, step_share=0.05):
        self.id = idx
        self.reserve_price = reserve  # in millions of roubles
        self.step_price = reserve * step_share
        self.min_price = None

    def set_min_price(self, price):
        if self.min_price is None or price < self.min_price:
            self.min_price = price

    def modify_reserve_price(self, modifier):
        self.reserve_price = max(self.reserve_price + self.step_price * modifier, 0)
        return self
