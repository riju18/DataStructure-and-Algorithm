def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    item_greater = []
    item_lower = []

    for item in arr:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)


arr_items = [5, 3, 1, 2, 4, 9, 0]
print(quick_sort(arr_items))
