from agents import Agent
from auctions import Auction
from items import Item


def create_items(step_share=0.05):
    """
    item ids 0, 1, 2, 4, 5, 6 respectively correspond to lots 1, 2-20, 21-22, 29-31, 32-36, 37-41
    """
    items = dict()

    idx = 0
    items[idx] = Item(idx, 1280, step_share=step_share)

    idx = 1
    items[idx] = Item(idx, 3390, step_share=step_share)

    idx = 2
    items[idx] = Item(idx, 4400, step_share=step_share)

    idx = 4
    items[idx] = Item(idx, 4230, step_share=step_share)

    idx = 5
    items[idx] = Item(idx, 4400, step_share=step_share)

    idx = 6
    items[idx] = Item(idx, 2290, step_share=step_share)

    return items


def create_agents():
    agents = dict()

    idx = 'a'
    agents[idx] = Agent(idx,
                        (0, 1, 1))

    idx = 'b'
    agents[idx] = Agent(idx,
                        (1, 12, 2))

    idx = 'c'
    agents[idx] = Agent(idx,
                        (0, 0, 1),
                        (1, 11, 2),
                        (2, 0, 1),
                        (4, 0, 1))

    idx = 'd'
    agents[idx] = Agent(idx,
                        (1, 11, 2))

    idx = 'E'
    agents[idx] = Agent(idx,
                        (1, 1, 2),
                        (2, 1, 1),
                        (4, 9, 1))

    idx = 'f'
    agents[idx] = Agent(idx,
                        (1, 3, 2))

    idx = 'G'
    agents[idx] = Agent(idx,
                        (1, 1, 1),
                        (4, 1, 1),
                        (5, 7, 2),
                        (6, 1, 3))

    idx = 'h'
    agents[idx] = Agent(idx,
                        (1, 4, 2),
                        (4, 8, 1))

    idx = 'K'
    agents[idx] = Agent(idx,
                        (0, 0, 1),
                        (1, 8, 8),
                        (2, 1, 1),
                        (4, 1, 1),
                        (5, 10, 1))

    idx = 'S'
    agents[idx] = Agent(idx,
                        (5, 11, 3),
                        (6, 1, 2))

    return agents


def correct_values(agents, items, step_share=0.05):
    for agent in agents.values():
        for item_id in agent.values.keys():
            agent.values[item_id] = items[item_id].reserve_price + \
                                    agent.values[item_id] * items[item_id].step_price * (0.05 / step_share) + 1e-3
    return agents


def create_auctions(agents, items, common=False):
    auctions = dict()

    item_id = 0
    reserve, step = items[item_id].reserve_price, items[item_id].step_price
    if common: agent_ids = [idx for idx in agents.keys() if item_id in agents[idx].items.keys()]

    idx = 1
    if not common: agent_ids = ['K', 'a', 'c']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    item_id = 1
    reserve, step = items[item_id].reserve_price, items[item_id].step_price
    if common: agent_ids = [idx for idx in agents.keys() if item_id in agents[idx].items.keys()]

    idx = 2
    if not common: agent_ids = ['K', 'd']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 3
    if not common: agent_ids = ['K', 'd', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 4
    if not common: agent_ids = ['K', 'b', 'd', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 5
    if not common: agent_ids = ['K', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 6
    if not common: agent_ids = ['K', 'b', 'c']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 7
    if not common: agent_ids = ['K', 'c', 'd', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 8
    if not common: agent_ids = ['K', 'b', 'd']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 9
    if not common: agent_ids = ['K', 'E', 'f']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 10
    if not common: agent_ids = ['K', 'c']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 11
    if not common: agent_ids = ['K', 'E', 'f', 'h']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 12
    if not common: agent_ids = ['K', 'c']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 13
    if not common: agent_ids = ['K', 'd', 'E', 'f']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 14
    if not common: agent_ids = ['K', 'd']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 15
    if not common: agent_ids = ['K', 'E', 'G']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 16
    if not common: agent_ids = ['K', 'c', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 17
    if not common: agent_ids = ['K', 'E', 'G']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 18
    if not common: agent_ids = ['K', 'E', 'f']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 19
    if not common: agent_ids = ['K', 'E', 'f', 'h']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 20
    if not common: agent_ids = ['K', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    item_id = 2
    reserve, step = items[item_id].reserve_price, items[item_id].step_price
    if common: agent_ids = [idx for idx in agents.keys() if item_id in agents[idx].items.keys()]

    idx = 21
    if not common: agent_ids = ['K', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 22
    if not common: agent_ids = ['K', 'c', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    item_id = 4
    reserve, step = items[item_id].reserve_price, items[item_id].step_price
    if common: agent_ids = [idx for idx in agents.keys() if item_id in agents[idx].items.keys()]

    idx = 29
    if not common: agent_ids = ['K', 'c', 'E']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 30
    if not common: agent_ids = ['K', 'E', 'h']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 31
    if not common: agent_ids = ['K', 'E', 'G']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    item_id = 5
    reserve, step = items[item_id].reserve_price, items[item_id].step_price
    if common: agent_ids = [idx for idx in agents.keys() if item_id in agents[idx].items.keys()]

    idx = 32
    if not common: agent_ids = ['K', 'G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 33
    if not common: agent_ids = ['K', 'G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 34
    if not common: agent_ids = ['K', 'G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 35
    if not common: agent_ids = ['K', 'G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 36
    if not common: agent_ids = ['K', 'G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    item_id = 6
    reserve, step = items[item_id].reserve_price, items[item_id].step_price
    if common: agent_ids = [idx for idx in agents.keys() if item_id in agents[idx].items.keys()]

    idx = 37
    if not common: agent_ids = ['G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 38
    if not common: agent_ids = ['G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 39
    if not common: agent_ids = ['G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 40
    if not common: agent_ids = ['G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    idx = 41
    if not common: agent_ids = ['G', 'S']
    auctions[idx] = Auction(idx, {i: agents[i] for i in agent_ids}, items[item_id], reserve, step, common)

    return auctions


def get_theoretical_profit(mode='cp'):
    """
    :param mode: 'cs' for common sequential or 'cp' for common parallel
    :return: total profit from the auction in theory
    """
    items = create_items()

    total_profit = 0
    if mode == 'cp':
        dct = {0: (0, 1),
               1: (1, 19),
               2: (1, 2),
               4: (1, 3),
               5: (7, 5),
               6: (1, 5)
               }  # idx: (price, quantity)
        for i in dct.keys():
            total_profit += items[i].reserve_price * dct[i][1] + items[i].step_price * dct[i][0] * dct[i][1]

    elif mode == 'cs':
        dct = {0: [0],
               1: [11, 11, 11, 11, 11, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               2: [1, 1],
               4: [8, 1, 1],
               5: [10, 10, 10, 7, 1],
               6: [1, 1, 1, 1, 1]
               }  # idx: [prices]
        for i in dct.keys():
            total_profit += items[i].reserve_price * len(dct[i]) + items[i].step_price * sum(dct[i])

    return total_profit
