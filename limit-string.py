# #CODEWARS 7kyu
# Truncate string to limit length and add "..."
# if string is shorter than limit, return string

def solution(st, limit): 
    if len(st) <= limit:
        return st
    
    slice = st[0:limit]
    return slice + "..."

# pseudocode
# if length of string is less than or equal to limit
# return string
# slice string to limit
# concat slice with "..."