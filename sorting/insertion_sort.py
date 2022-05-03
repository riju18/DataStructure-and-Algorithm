class InsertionSort:

    def __init__(self):
        self.numberList = list()

    def insertNum(self, val):
        self.numberList.append(val)

    def showAscending(self):

        # main logic
        # --------------

        for i in range(1, len(self.numberList)):
            val = self.numberList[i]
            j = i
            while j > 0 and self.numberList[j - 1] > val:
                self.numberList[j] = self.numberList[j - 1]
                j -= 1
            self.numberList[j] = val

        print(self.numberList)

    def showDescending(self):

        # main logic
        # --------------

        for i in range(1, len(self.numberList)):
            val = self.numberList[i]
            j = i
            while j > 0 and self.numberList[j - 1] < val:
                self.numberList[j] = self.numberList[j - 1]
                j -= 1
            self.numberList[j] = val

        print(self.numberList)


if __name__ == '__main__':
    i_sort = InsertionSort()

    i_sort.insertNum(8)
    i_sort.insertNum(5)
    i_sort.insertNum(13)
    i_sort.insertNum(11)
    i_sort.insertNum(2)
    i_sort.insertNum(7)

    print('in ascending:\n')
    i_sort.showAscending()
    print('\n in descending:\n')
    i_sort.showDescending()
