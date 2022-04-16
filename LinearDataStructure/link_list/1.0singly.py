class Node:  # 1
    def __init__(self, val):
        self.value = val
        self.next = None  # initially there is 1 node in link list, so no reference


class linkedList:  # 2
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
                print(f"Position: {ind}, value:{current.value}")
                break
            pos += 1
            current = current.next

    def showPosByVal(self, val):
        pos = 0
        current = self.start
        while current:
            if current.value == val:
                print(f"Value: {val}, position: {pos}")
                break
            pos += 1
            current = current.next

    def reverse_linked_list(self):
        current_node = self.start
        previous_node = None
        next_node = None
        while current_node:
            next_node, current_node.next = current_node.next, previous_node
            previous_node, current_node = current_node, next_node

        current = previous_node
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    linkList = linkedList()
    linkList.insert(2)
    linkList.insert(5)
    linkList.insert(3)
    linkList.insert(1)
    linkList.show()
    linkList.showByPos(1)
    linkList.showPosByVal(5)
    linkList.reverse_linked_list()
