def linearSearch(listItem, key):
    flag = False
    position = 0
    while position < len(listItem) and not flag:
        if listItem[position] == key:
            flag = True
        else:
            position += 1

    return flag


demoList = [84, 21, 47, 96, 15]
flag = linearSearch(demoList, 96)
if flag is True:
    print('key found..')
else:
    print('key not found..')