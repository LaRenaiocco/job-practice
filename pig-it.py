#Code Wars (5kyu) pig latinify a text phrase.
#account for punctuation which will be separated by space
string1 = 'Pig latin is cool'
string2 = 'Hello world !'

def pig_it(text):
    words = text.split()
    pig_words = []
    for word in words:
        # if word is alpha pigify it.
        if word.isalpha():
            first = word[0:1]
            end = word[1:]
            word = end + first + 'ay'
            pig_words.append(word)
        else:     # adds punctuatin marks back to list
            pig_words.append(word)
    result = ' '.join(pig_words)
    return result
#     split words into list
#     for each word in list
#     check if first letter is alpha
#     pop off first letter
#     add letter to end of word
#     add 'ay' to end of work

pig_it(string2)