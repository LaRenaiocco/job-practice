# A prime number is a number >= 2 that is only evenly divisible by itself and 1.

# So, for example, 3 is a prime number but 4 (divisible by 2) is not. The first few primes are: 2, 3, 5, 7, 11.

# Write a function that produces count prime numbers, where count is a value passed into the function.

def primes(count):
    """Return count number of prime numbers, starting at 2.
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]
    """
