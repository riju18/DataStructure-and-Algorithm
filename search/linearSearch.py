def linearSearch(listItem, key):
    flag = False
    position = 0
    while position < len(listItem) and not flag:
        if listItem[position] == key:
            flag = True
        position += 1

    return flag


# or,

def linearSearch1(listItem, key):
    flag = False
    for i in listItem:
        if i == key:
            flag = True
            break

    return flag


demoList = [84, 21, 47, 96, 15]
result = 'key found..' if linearSearch1(demoList, 96) is True else 'key not found..'
print(result)
