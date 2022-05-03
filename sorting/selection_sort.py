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
                    self.numberList[minValIndex], self.numberList[j] = self.numberList[j], self.numberList[minValIndex]
        print(self.numberList)

    def showDescending(self):
        for i in range(0, len(self.numberList) - 1):
            maxValIndex = i
            for j in range(i + 1, len(self.numberList)):
                if self.numberList[maxValIndex] < self.numberList[j]:
                    self.numberList[maxValIndex], self.numberList[j] = self.numberList[j], self.numberList[maxValIndex]
        print(self.numberList)


if __name__ == '__main__':
    s_sort = selectionSort()
    
    s_sort.insertVal(90)
    s_sort.insertVal(35)
    s_sort.insertVal(60)
    s_sort.insertVal(7)
    s_sort.insertVal(2)
    s_sort.insertVal(3)
    s_sort.insertVal(89)
    
    s_sort.showAscending()
    s_sort.showDescending()
