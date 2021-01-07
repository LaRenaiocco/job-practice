# Who is the killer?
# Some people have been killed!
# You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

# Task.
# Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

# {'James': ['Jacob', 'Bill', 'Lucas'],
#  'Johnny': ['David', 'Kyle', 'Lucas'],
#  'Peter': ['Lucy', 'Kyle']}
# and also a list of the names of the dead people:

# ['Lucas', 'Bill']
# return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

#pseudocode
# iterate through the dictionary keys
# for each key
# for each person in killed list
# check if killed is in value array of key
# if yes, return Key 
def killer(suspect_info, dead):
    """
    >>> killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'],'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill'])
    'James'
    """
    killed_tally = len(dead)

    for suspect in suspect_info:
        contacts_tally = 0
        for person in dead:
            if person in suspect_info[suspect]:
                contacts_tally += 1
        if contacts_tally == killed_tally:
            return suspect
        

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')