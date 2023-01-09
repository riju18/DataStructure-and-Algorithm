def binarySearch(l, key):
    low = 0
    high = len(l) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if l[mid] == key:
            found = True
        elif key < l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return found


demoList = [84, 21, 47, 96, 15]
demoList.sort()
flag = binarySearch(demoList, 21)
if flag:
    print('key found..')
else:
    print('key not found..')
