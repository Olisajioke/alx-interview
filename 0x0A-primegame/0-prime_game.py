#!/usr/bin/python3
"""A module for solving the Prime Game problem."""


def isWinner(x, nums):
    """Determine who the winner of the game is."""
    def sieve_of_eratosthenes(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return sum(sieve)

    maria_wins, ben_wins = 0, 0

    for n in nums:
        if sieve_of_eratosthenes(n) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    return ("Maria" if maria_wins > ben_wins else
            "Ben" if ben_wins > maria_wins else
            None)