class Queue:
    def __init__(self):
        self.qu = list()
        # ************
        # Empty queue
        # ************
        self.first = -1
        self.last = -1

    def nq(self, val):
        if self.first == -1:
            self.first += 1
        self.last += 1
        self.qu.insert(self.last, val)

    def dq(self, ind):
        try:
            # find the index of value
            index = self.qu.index(ind)
            del self.qu[index]
        except:
            print('index error !!!!!!!! \n ')

    def show(self):
        for i in self.qu:
            print(i, end=' ')


q = Queue()

# enter value
q.nq(3)
q.nq(5)
q.nq(9)

# delete value
q.dq(3)

# show queue
q.show()
