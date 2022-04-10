s = "(()())(())(()(()))"
opening_paren = set('({[')
paren_pair = [('(', ')'), ('{', '}'), ('[', ']')]
stack = []
for i in s:
    if i in opening_paren:
        print(f"{i} in opening paren")
        stack.append(i)
    else:
        print(f"{i} in closing paren")
        open_paren = stack.pop()
        if (open_paren, i) not in paren_pair:
            print(f"pair paren is not matched")
            pass
if len(stack) == 0:
    print(True)
else:
    print(False)
