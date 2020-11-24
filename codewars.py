#Form the Largest (7kyu)
def max_number(n):
    nums_list = sorted([num for num in str(n)], reverse = True)
    return int("".join(nums_list))

#Minimize sum or array (7kyu)
def min_sum(arr):
    sorted_list = sorted(arr)
    print(sorted_list)
    sums_list = []
    while len(sorted_list) > 0:
        sums_list.append(sorted_list[0] * sorted_list[-1])
        sorted_list.pop(0)
        sorted_list.pop(-1)
    return sum(sums_list)

#Find Screen Size (7kyu)
def find_screen_height(width, ratio): 
    ratio = ratio.split(":")
    w, h = ratio
    height = int((width / int(w)) * int(h))
    return f"{width}x{height}"

#Multiplication table for number (8kyu)
def multi_table(number):
    string = ''
    for num in range(1,11):
        total = num * number
        summation = f'{num} * {number} = {total}'
        string += summation
        if num != 10:
            string += '\n'
    return string


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
    
