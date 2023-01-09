# ************************
# Principle
# ============
# FIFO: First in first out
# EX: ticket line
# *************************


class Queue:
    def __init__(self):
        self.items = []

    def nq(self, i):
        self.items.append(i)
        print(f"After nq: {self.items}")

    def dq(self):
        self.items.pop(0)
        print(f"after dq: {self.items}")

    def getItems(self):
        print(f"All items: {self.items}")

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.nq(1)
    q.nq(2)
    q.nq(3)

    q.dq()
    q.dq()

    q.getItems()
    print(f"Item size: {len(q)}")

