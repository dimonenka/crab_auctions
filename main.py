from mechanisms import Sequential, Parallel
from utils import create_agents, create_items, create_auctions, correct_values

import numpy as np


if __name__ == '__main__':
    PARALLEL = False
    COMMON = False
    N_RUNS = 1000
    QUANTILE = 0.005
    STEP_SHARE = 0.05
    VERBOSE = False

    prices, regrets = [], []
    for i in range(N_RUNS):
        items = create_items(STEP_SHARE)

        agents = create_agents()
        ### agents = {k: v.modify_capacities(0) for k, v in agents.items()}
        ### agents = {k: v.modify_values(0) for k, v in agents.items()}
        agents = correct_values(agents, items, step_share=STEP_SHARE)

        ### items = {k: v.modify_reserve_price(0) for k, v in items.items()}

        auctions = create_auctions(agents, items, COMMON)
        auctions = {k: v.check_agents() for k, v in auctions.items()}

        mechanism = Parallel(agents, items, auctions) if PARALLEL else Sequential(agents, items, auctions)
        price = mechanism.run(VERBOSE)
        prices.append(price)
        regret = mechanism.get_regret()
        regrets.append(regret)

    low_price, avg_price, high_price = np.quantile(prices, QUANTILE), np.mean(prices), np.quantile(prices, 1 - QUANTILE)
    low_price, avg_price, high_price = round(low_price/1000, 1), round(avg_price/1000, 1), round(high_price/1000, 1)
    print('parallel' if PARALLEL else 'sequential', 'common:' if COMMON else 'individual',
          '\nprice', avg_price, 'bln rub, ci [', low_price, ',', high_price, '] bln rub')

    low_rgt, avg_rgt, high_rgt = np.quantile(regrets, QUANTILE), np.mean(regrets), np.quantile(regrets, 1 - QUANTILE)
    low_rgt, avg_rgt, high_rgt = round(low_rgt / 1000, 1), round(avg_rgt / 1000, 1), round(high_rgt / 1000, 1)
    print('regret', avg_rgt, 'bln rub, ci [', low_rgt, ',', high_rgt, '] bln rub')
