class Node:     # 1
    def __init__(self, val):
        self.value = val
        self.next = None  # initially there is 1 node in link list, so no reference


class linkedList:       # 2
    def __init__(self):
        self.start = None  # initially the node is empty

    def insert(self, val):
        if self.start is None:
            self.start = Node(val)
            return
        current = self.start
        while current.next:
            current = current.next
        current.next = Node(val)

    def show(self):
        current = self.start
        while current:
            print(current.value)
            current = current.next

    def showByPos(self, ind):
        pos = 0
        current = self.start
        while current:
            if pos == ind:
                print(current.value)
            pos += 1
            current = current.next

    def showPosByVal(self, val):
        pos = 0
        current = self.start
        while current:
            if current.value == val:
                print(pos)
            pos += 1
            current = current.next


linkList = linkedList()
linkList.insert(2)
linkList.insert(5)
linkList.insert(3)
linkList.show()
linkList.showByPos(1)
linkList.showPosByVal(5)
