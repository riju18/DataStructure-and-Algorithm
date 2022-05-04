def linearSearch(listItem, key):
    flag = False
    position = 0
    while position < len(listItem) and not flag:
        if listItem[position] == key:
            flag = True
        position += 1

    return flag


demoList = [84, 21, 47, 96, 15]
result = 'key found..' if linearSearch(demoList, 96) is True else 'key not found..'
print(result)
