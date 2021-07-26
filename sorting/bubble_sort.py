def bubbleSort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


arr = [84, 21, 96, 15, 47]
bubbleSort(arr)
print(arr)