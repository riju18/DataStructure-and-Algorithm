def binarySearch(list, key):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == key:
            return True
        elif key < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


demoList = [84, 21, 47, 96, 15]
demoList.sort()
flag = binarySearch(demoList, 16)
if flag is True:
    print('key found..')
else:
    print('key not found..')
