import numpy as np


class Auction:
    def __init__(self, idx, agents, item, reserve=0, step=1, common=False):
        self.id = idx
        self.reserve_price = reserve
        self.step_price = step
        self.current_price = reserve
        self.item = item
        self.item_id = item.id
        self.agents = agents
        self.agent_ids = list(agents.keys())
        np.random.shuffle(self.agent_ids)
        self.winner_id = None
        self.common = common  # True if the auction is for all agents who have not reached capacity of this item

    @property
    def next_price(self):
        return self.current_price + self.step_price

    def step(self, winner_id=None):
        if winner_id is not None:
            self.set_winner(winner_id)

        self.current_price += self.step_price

    def set_winner(self, agent_id):
        self.winner_id = agent_id

    def finish(self, winner_id=None):
        self.item.set_min_price(self.current_price)

        if winner_id is not None:
            self.set_winner(winner_id)

        if self.winner_id is None:
            if len(self.agents) == 0:  # no one registered
                return 0
            else:  # earliest registered (implemented as random) participant
                if not self.common:
                    winner_id = self.agent_ids[0]
                    self.set_winner(winner_id)
                else:
                    for winner_id in self.agent_ids:
                        if self.agents[winner_id].check_capacity(self.item_id):  # also check if someone is eligible for the item
                            self.set_winner(winner_id)
                            break
                        if winner_id == self.agent_ids[-1]:  # otherwise it is not sold
                            return 0
        self.agents[self.winner_id].add_item(self.item_id)
        return self.current_price

    def run(self):
        agents = {idx: a for idx, a in self.agents.items() if a.check_item(self.item_id, self.next_price)}  # agents that want to bid
        if len(agents) == 0:
            return self.finish()

        while len(agents) > 1 or self.winner_id is None:
            agent = np.random.choice(list(agents.values()), 1)[0]
            if agent.id != self.winner_id:
                if agent.check_item(self.item_id, self.next_price):
                    self.step(agent.id)
                else:
                    agents.pop(agent.id)
        return self.finish()

    def check_agents(self):
        for agent_id, agent in self.agents.items():
            if (agent.values[self.item_id] < self.reserve_price) or (agent.capacities[self.item_id] <= 0):
                self.agent_ids.remove(agent_id)
        self.agents = {k: v for k, v in self.agents.items() if k in self.agent_ids}
        return self
