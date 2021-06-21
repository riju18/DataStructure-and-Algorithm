def recursion_sum(num):
    if num == 1:
        return 1
    else:
        return num + recursion_sum(num - 1)


n = 4
if n < 0:
    print('invalid')
elif n == 0:
    print(0)
else:
    print(recursion_sum(n))
