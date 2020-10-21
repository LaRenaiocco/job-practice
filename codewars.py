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
    
