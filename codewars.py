#Remove B M W (7kyu)
def remove_bmw(string):
    try:
        bmw = {"b", "m", "w"}
        result = ""
        for char in string:
            if char.lower() not in bmw:
                result += char
        return result
    except:
        if type(string) != str:
            return "This program only works for text."

#Shortest Word (7kyu)
def find_short(s):
    words = s.split()
    shortest = len(words[0])
    for word in words:
        if len(word) < shortest:
            shortest = len(word)
    return shortest 

#Dubstep (6 kyu)
def song_decoder(song):
    words = song.split("WUB")
    og_song = ""
    for word in words:
        if word != "":
            og_song += word
            og_song += " "

    return og_song.strip(" ")

# Remove the Parentheses (6 kyu)
def remove_parentheses(s):

    parens = 0
    result = ""
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        else:
            if parens == 0:
                result += char
    return result
    
