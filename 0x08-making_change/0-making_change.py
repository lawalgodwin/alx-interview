#!/usr/bin/python3
""" Making changes
"""


def makeChange(coins, total):
    """ find the minimum(fewest) number of coins needed to make up the
    amount(total)
    Time: O(nlogn)
    """
    change = 0

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    for coin in coins:
        increase = (total // coin)
        total -= (increase * coin)
        change += increase
        if total == 0:
            return change

    return -1
