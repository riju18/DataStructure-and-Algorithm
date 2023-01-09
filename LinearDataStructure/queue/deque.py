# *************************************************
# Principle
# ============
# new items can be added/removed either front/rear
# ************************************************


class Queue:
    def __init__(self):
        self.items = []

    def addFront(self, i):  # nq
        self.items.append(i)
        print(f"After add front: {self.items}")

    def addRear(self, i):
        self.items.insert(0, i)
        print(f"After add rear: {self.items}")

    def removeFront(self):
        self.items.pop()
        print(f"After remove front: {self.items}")

    def removeRear(self):   # dq
        self.items.pop(0)
        print(f"after remove rear: {self.items}")

    def getItems(self):
        print(f"All items: {self.items}")

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.addFront(1)
    q.addFront(2)
    q.addFront(3)

    q.addRear(4)
    q.addRear(5)
    q.addRear(6)

    q.removeFront()
    q.removeRear()

    q.getItems()
    print(f"Item size: {len(q)}")
