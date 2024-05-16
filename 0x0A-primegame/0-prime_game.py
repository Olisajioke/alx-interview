#!/usr/bin/python3
"""A module for solving the Prime Game problem."""


def isWinner(x, nums):
    """Find the winner of the game"""
    def is_prime(num):
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(start):
        """Find the next prime number after start"""
        start += 1  # Start searching from the next number
        while True:
            if is_prime(start):
                return start
            start += 1

    def play_round(n):
        """Play a round of the game"""
        maria_turn = True
        while n > 1:
            prime = get_next_prime(2)
            if maria_turn:
                n -= prime
            else:
                n -= prime * (n // prime)
            maria_turn = not maria_turn
        return "Maria" if maria_turn else "Ben"

    winners = []
    for n in nums:
        winners.append(play_round(n))

    # Count the winners
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None