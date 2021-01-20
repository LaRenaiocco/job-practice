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

    if count == 0:
        return []
    if count == 1:
        return [2]
    current = 3
    result = [2]
    while len(result) < count:
        prime = True
        if current % 2 == 0:
            prime = False
        else:
            half_curr = (current // 2) + 1
            for num in range(2, half_curr):
                if current % num == 0:
                    prime = False
            if prime == True:
                result.append(current)
        current += 1

    return result






if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')