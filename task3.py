def correct(string):
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '').replace('{}', '').replace('[]', '')
    if len(string) == 0:
        return True
    else:
        return False

def correct2(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append(']')
        elif len(stack) == 0 or stack.pop() != i:
            return False
    return len(stack) == 0