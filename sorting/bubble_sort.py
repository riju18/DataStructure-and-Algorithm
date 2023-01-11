def bubble_sort(x):
    count = 0
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                count += 1
                x[j], x[j + 1] = x[j + 1], x[j]
    print(f'no of times swapped for ascending order: {count}')


def bubble_sort_desc(x):
    count = 0
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] < x[j + 1]:
                count += 1
                x[j + 1], x[j] = x[j], x[j + 1]
    print(f'no of times swapped for descending order: {count}')


arr = [84, 21, 96, 15, 47]
bubble_sort(arr)
print(f"ascending order: {arr}")
bubble_sort_desc(arr)
print(f"descending order: {arr}")