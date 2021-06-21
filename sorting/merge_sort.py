def mergeSort(x):
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0   # left half
        j = 0   # right half
        k = 0   # final list

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1


arr = [84, 21, 96, 15, 47]
mergeSort(arr)
print(arr)
