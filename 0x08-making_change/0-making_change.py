#!/usr/bin/python3

"""
Module for making change with the fewest number of coins
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given total amount

    :param coins: List of coin values
    :param total: Total amount to make change for
    :return: Fewest number of coins needed, or -1 if total cannot be met
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
