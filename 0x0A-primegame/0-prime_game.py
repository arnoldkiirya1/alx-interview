#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Function to determine the winner of the prime game"""
    if not nums or x < 1:
        return None

    def is_prime(n):
        """Check if a number is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # Counts the number of rounds won by each player
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
