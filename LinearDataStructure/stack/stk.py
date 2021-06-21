# ***************************
# stack: LIFO/FILO
# LIFO: last in first out
# FILO: first in last out
# ***************************


class Stack:
    def __init__(self):
        self.stack = list()

    def insertVal(self, val):
        self.stack.append(val)

    def delVal(self):
        if len(self.stack) > 1:
            self.stack.pop()

    def show(self):
        print(self.stack)


st = Stack()
st.insertVal(3)
st.insertVal(5)
st.insertVal(7)
st.insertVal(9)

st.delVal()

st.show()
