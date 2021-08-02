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


sortt = InsertionSort()

sortt.insertNum(8)
sortt.insertNum(5)
sortt.insertNum(13)
sortt.insertNum(11)
sortt.insertNum(2)
sortt.insertNum(7)

print('in ascending:\n')
sortt.showAscending()
print('\n in descending:\n')
sortt.showDescending()
