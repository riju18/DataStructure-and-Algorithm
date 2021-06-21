class selectionSort:
    def __init__(self):
        self.numberList = list()

    def insertVal(self, val):
        self.numberList.append(val)

    def showAscending(self):
        # main logic
        # --------------

        for i in range(0, len(self.numberList) - 1):
            minValIndex = i
            for j in range(i + 1, len(self.numberList)):
                if self.numberList[minValIndex] > self.numberList[j]:
                    temp = self.numberList[minValIndex]
                    self.numberList[minValIndex] = self.numberList[j]
                    self.numberList[j] = temp
        print(self.numberList)

    def showDescending(self):
        for i in range(0, len(self.numberList) - 1):
            maxValIndex = i
            for j in range(i + 1, len(self.numberList)):
                if self.numberList[maxValIndex] < self.numberList[j]:
                    temp = self.numberList[maxValIndex]
                    self.numberList[maxValIndex] = self.numberList[j]
                    self.numberList[j] = temp
        print(self.numberList)


ssort = selectionSort()

ssort.insertVal(90)
ssort.insertVal(35)
ssort.insertVal(60)
ssort.insertVal(7)
ssort.insertVal(2)
ssort.insertVal(3)
ssort.insertVal(89)

ssort.showAscending()
ssort.showDescending()
