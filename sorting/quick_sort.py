def quick_sort_asc(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()

    item_greater = []
    item_lower = []

    for item in arr:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    return quick_sort_asc(item_lower) + [pivot] + quick_sort_asc(item_greater)


def quick_sort_dsc(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()

    item_greater = []
    item_lower = []

    for item in arr:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    return quick_sort_dsc(item_greater) + [pivot] + quick_sort_dsc(item_lower)


arr_items = [5, 3, 1, 2, 4, 9, 0]
arr_items1 = [5, 3, 1, 2, 4, 9, 0]
print(quick_sort_asc(arr_items))
print(quick_sort_dsc(arr_items1))
