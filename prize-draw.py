# To participate in a prize draw each one gives his/her firstname.

# Each letter of a firstname has a value which is its rank in the 
# English alphabet. A and a have rank 1, B and b rank 2 and so on.

# The length of the firstname is added to the sum of these ranks 
# hence a number som.

# An array of random weights is linked to the firstnames and each 
# som is multiplied by its corresponding weight to get what they 
# call a winning number.

# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]

# PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
# The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.
# Now one can sort the firstnames in decreasing order of the winning numbers. 
# When two people have the same winning number sort them alphabetically 
# by their firstnames.

# Task:
# parameters: st a string of firstnames, we an array of weights, n a rank

# return: the firstname of the participant whose rank is n (ranks are numbered from 1)

# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]
# n: 4

# The function should return: "PauL"
# Notes:
# The weight array is at least as long as the number of names, 
# it may be longer.

# If st is empty return "No participants".

# If n is greater than the number of participants then return 
# "Not enough participants".

from collections import OrderedDict
def rank(st, we, n):
    """
    >>> rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 4)
    'PauL'
    >>> rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
    'Benjamin'
    >>> rank("Lagon,Lily", [1, 5], 2)
    'Lagon'
    >>> rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8)
    'Not enough participants'
    >>> rank("", [4, 2, 1, 4, 3, 1, 2], 6)
    'No participants'
    """
    if len(st) == 0:
        return 'No participants'

    names = st.split(',')

    if len(names) < n:
        return 'Not enough participants'

    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                    'y': 25, 'z': 26}
    name_scores = {}
    for index, name in enumerate(names):
        name_scores[name] = name_scores.get(name, 0)
        for char in name:
            name_scores[name] += letter_values[char.lower()]
        name_scores[name] *= we[index]
    sorted_names = sorted(name_scores, key=name_scores.__getitem__, reverse=True)
    return sorted_names[n - 1]
        


# pseudocode:
# quick break if participants string is empty, return 'no participants'
# break apart the participants string into a list
# use .split method, splitting on commas
# quick break #2
# if length of participants list is less than n, return 'not enough participants'
# create a dictionary where keys will be names and values will be soms 
# loop through names list with enumerate
# for each name, add to dictionary.
# for each letter in each name:
#     find value of letter, add to value in dictionary
# multiply complete value by weight in weight list,
# which we can get by using matching index points
# sort names in dictionary by values
# so we can return the person at rank num

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')