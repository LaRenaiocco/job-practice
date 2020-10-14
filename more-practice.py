#Repeated String HackerRank interview prep
def repeatedString(s, n):
    length = len(s)
    num_a = 0
    for char in s:
        if char == "a":
            num_a += 1
    complete_strings = n // length
    result = complete_strings * num_a
    extra = n % length
    last_slice = s[:extra]
    for char in last_slice:
        if char == "a":
            result += 1
    return result

#sort odds in numerical order but leave evens where they are in array
def sort_array(source_array):
    odds = []
    odds_index = []
    for i, num in enumerate(source_array):
        if num % 2 != 0:
            odds.append(num)
            odds_index.append(i)
    odds.sort()
    while odds != []:
        i = odds_index.pop(0)
        num = odds.pop(0)
        source_array[i] = num
    return source_array

#encode a message using rot13 ceaser cipher
def rot13(message):
    alpha = {
        "a": "n", "A": "N", "b": "o", "B": "O", "c": "p", "C": "P", 
        "d": "q", "D": "Q", "e": "r", "E": "R", "f": "s", "F": "S",
        "g": "t", "G": "T", "h": "u", "H": "U", "i": "v", "I": "V",
        "j": "w", "J": "W", "k": "x", "K": "X", "l": "y", "L": "Y",
        "m": "z", "M": "Z", "n": "a", "N": "A", "o": "b", "O": "B",
        "p": "c", "P": "C", "q": "d", "Q": "D", "r": "e", "R": "E",
        "s": "f", "S": "F", "t": "g", "T": "G", "u": "h", "U": "H",
        "v": "i", "V": "I", "w": "j", "W": "J", "x": "k", "X": "K",
        "y": "l", "Y": "L", "z": "m", "Z": "M"
        }
    result = ""
    for char in message:
        new = alpha.get(char, None)
        if new == None:
            result += char
        else: 
            result += new
    return result

def areYouPlayingBanjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

def mirror(data: list) -> list:
    result = sorted(data)
    reversed = sorted(data, reverse = True)
    result.extend(reversed[1:])
    return result

def flip(d, a):
    if d == "R":
        result = sorted(a)
    else:
        result = sorted(a, reverse = True)
    return result

# will the number of bullets kill all the dragons if it takes
# two bullets to kill a dragon
def hero(bullets, dragons):
    if bullets / 2 >= dragons:
        return True
    else: 
        return False

#is a number divisible by 2 other numbers
def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0

#remove adjacent duplicate characters from a string
def solution(stones):
    count = 0
    index = 0
    end = len(stones) - 1
    while index < end:
        if stones[index] == stones[index + 1]:
            count += 1
        index += 1
        
    return count

#remove vowels from a string
def disemvowel(string):
    vowels = "AEIOUaeiou"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result

# return characters at specific index points on a grid (codewars
def grid_index(grid, indexes):
    l = []
    result =""
    for row in grid:
        l.extend(row)
    for num in indexes:
        result += l[num - 1]
        
    return result

# check how many times the letter a is present n length of string s, repeated infinitely
def repeatedString(s, n):
    """
    >>> repeatedString('abc', 10)
    4
    """
    length = len(s)
    num_a = 0
    for char in s:
        if char == "a":
            num_a += 1
    complete_strings = n // length
    result = complete_strings * num_a
    extra = n % length
    last_slice = s[:extra]
    for char in last_slice:
        if char == "a":
            result += 1
    return result
    #/ check the length of the string 
    ## check and record what index points are an a 
    #/ record how many As
    #/ divide n by length of string to know how many complete strings
    #/ multipy complete strings by number of As 
    #/ check how many left over characters with Modulo 
    # check for a's in the leftover characters.
    # add to total as 
    # return total

def word_lengths(sentence):
    """Given a phrase, return dictionary keyed by word-length, 
    with the value for each length being the set of words of that length.
    Get dictionary of word-length: {words}.
    """
    word_list = sentence.split()
    result = {}
    for word in word_list:
        length = len(word)
        result[length] = result.get(length, set())
        result[length].add(word)
    return result


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    from random import randint
    result = []
    while len(result) < n:
        random_num = randint(1, 10)
        if random_num not in result:
            result.append(random_num)
    return result


def compress(string):
    """Return a compressed version of the given string.
    Write a function that compresses a string.

    Repeated characters should be compressed to one character and the number of
    times it repeats:

    >>> compress('aabbaabb')
    'a2b2a2b2'

    If a character appears once, it should not be followed by a number:

    >>> compress('abc')
    'abc'

    The function should handle letters, whitespace, and punctuation:

    >>> compress('Hello, world! Cows go moooo...')
    'Hel2o, world! Cows go mo4.3'
    """
    char_list = []
    for char in string:
        char_list.append(char)
    new_list = [char_list[0]]
    index = 0
    count = 1
    while index < len(char_list)-1:
        if char_list[index] == char_list[index + 1]:
            count += 1
        else:
            if count != 1:
                new_list.append(str(count))
                count = 1
            new_list.append(char_list[index + 1])
        index += 1
    if count != 1:
        new_list.append(str(count))
    new_string = "".join(new_list)
    return new_string

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')

