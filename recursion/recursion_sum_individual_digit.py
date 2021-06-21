def recursion_logic(num):
    if len(str(num)) == 1:
        return num
    else:
        return int(num % 10) + recursion_logic(num // 10)


n = 4321
print(recursion_logic(n))
