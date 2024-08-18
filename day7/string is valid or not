def is_valid_brackets(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False
        else:
            continue
    return stack == []
print(is_valid_brackets("()"))       
print(is_valid_brackets("()[]{}"))  
print(is_valid_brackets("(]"))        
print(is_valid_brackets("([)]"))      
print(is_valid_brackets("{[]}"))
