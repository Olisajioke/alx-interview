#!/usr/bin/python3
"""A module for solving the Prime Game problem."""


def isWinner(x, nums):
    """
    Determine the winner of a game where Maria and Ben play x rounds of a game
    """
    def sieve_of_eratosthenes(limit):
        """
        Generate all prime numbers up to a given limit using the
        Sieve of Eratosthenes algorithm.
        """
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return [i for i in range(limit + 1) if sieve[i]]

    def count_primes_up_to_n(n):
        """
        Count the number of prime numbers up to n.
        """
        primes = sieve_of_eratosthenes(n)
        return len(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers up to n
        primes_count = count_primes_up_to_n(n)

        # If the count is odd, Maria wins; otherwise, Ben wins
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
