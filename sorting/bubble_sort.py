def bubbleSort(x):
    count = 0
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                count += 1
                x[j], x[j + 1] = x[j + 1], x[j]
    print(f'no of times swapped: {count}')


arr = [84, 21, 96, 15, 47]
bubbleSort(arr)
print(arr)