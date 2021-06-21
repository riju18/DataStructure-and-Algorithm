def recur(n):
    if n == 1:
        return n
    else:
        return n * recur(n - 1)


num = 5
if num < 0:
    print('invalid number')
elif num == 0:
    print('factorial: ', 1)
else:
    print('factorial: ', recur(num))
