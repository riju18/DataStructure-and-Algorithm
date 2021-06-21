def recursion_logic(num):
    if len(num) == 1:
        return num
    else:
        return recursion_logic(num[1:]) + num[0]


n = 'abc'
print(recursion_logic(n))
