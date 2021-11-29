import numpy as np


class Sequential:
    def __init__(self, agents, items, auctions):
        self.agents = agents
        self.items = items
        self.auctions = auctions

    def run(self, verbose=False):
        total_price = 0
        for idx, auction in self.auctions.items():
            total_price += auction.run()
        if verbose:
            print({a.id: a.items for a in self.agents.values()})
        return total_price

    def get_regret(self):
        regret = 0
        for auction in self.auctions.values():
            regret += max(auction.current_price - self.items[auction.item_id].min_price, 0)
        return regret


class Parallel(Sequential):
    def __init__(self, agents, items, auctions):
        super().__init__(agents, items, auctions)

    def run(self, verbose=False):
        agents = list(self.agents.values())

        done = False
        while not done:
            done = True
            np.random.shuffle(agents)
            for agent in agents:
                best_profit, best_id = 0, None
                for idx, auction in self.auctions.items():
                    if agent.id in auction.agent_ids and agent.check_item(auction.item_id, auction.next_price) and \
                            auction.winner_id != agent.id:
                        profit = agent.values[auction.item_id] - auction.next_price
                        if profit >= best_profit:
                            best_profit, best_id = profit, idx
                            done = False
                if best_id is not None:
                    prev_winner_id = self.auctions[best_id].winner_id
                    item_id = self.auctions[best_id].item_id
                    self.auctions[best_id].step(agent.id)
                    agent.add_item(item_id)
                    if prev_winner_id is not None:
                        self.agents[prev_winner_id].remove_item(item_id)

        total_price = 0
        for auction in self.auctions.values():
            if auction.winner_id is not None:
                self.agents[auction.winner_id].remove_item(auction.item_id)
            total_price += auction.finish()
        if verbose:
            print({a.id: a.items for a in self.agents.values()})
        return total_price
