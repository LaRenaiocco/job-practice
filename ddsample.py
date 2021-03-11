# given an array of values, write a function that outputs all 
# prime numbers that include the second number of my birthday

def primes(nums, birthday):
    """
    >>> primes([ 3, 4, 5, 13, 30, 63], 23)
    [3, 13]
    """
    bd_2 = str(birthday)[-1]
    result = []
    for num in nums:
        if check_prime(num):
            if bd_2 in str(num):
                result.append(num)
    return result
        


# pseudocode:
# establish the number to check by converting birthday to string and 
# setting last index to a variable
# create an emptry list for result
# for each number in list:
#     use helper function to check for prime
#     if helper function returns true, then do the following
#     convert num to a string
#     check if last birthday num is in prime num
#     if yes, 
#     convert back to int and add to list
# return result list

def check_prime(num):
    """
    >>> check_prime(1)
    False
    >>> check_prime(2)
    True
    >>> check_prime(13)
    True
    >>> check_prime(10)
    False
    """
    if num == 1:
        return False
    if num == 2:
        return True
    halfway = num // 2
    divisor = 2
    while divisor <= halfway:
        if num % divisor == 0:
            return False
        else:
            divisor += 1
    return True


# create a helper function to check if a number is a prime
# establish halfway point of num 
# if number is 1 return false
# if number is 2 return true
# half variable = num // 2
# start num = 2
# while start num is less than half variable do the following
# check if number % start num is equal to 0
# if yes, return False
# if no, increase start num by 1
# at the end, return True

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')