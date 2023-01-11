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
            print(current.value, end=' ')
            current = current.next
        print('\n')

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

    def get_length(self):
        current = self.start
        c = 0
        while current:
            current = current.next
            c += 1
        print(f"Length of linked list is: {c}")

    def last_node(self):
        current = self.start
        last_node_val = None
        if current:
            while current:
                if current.next is None:
                    last_node_val = current.value
                current = current.next
        print(f"Last node is: {last_node_val}")

    def reverse_linked_list(self):
        current_node = self.start
        previous_node = None
        next_node = None
        while current_node:
            next_node, current_node.next = current_node.next, previous_node
            previous_node, current_node = current_node, next_node

        current = previous_node
        while current:
            print(current.value, end=' ')
            current = current.next
        print('\n')


if __name__ == '__main__':
    linkList = linkedList()
    linkList.insert(2)
    linkList.insert(5)
    linkList.insert(3)
    linkList.insert(1)
    print("Original linked list: ")
    linkList.show()
    linkList.showByPos(1)
    linkList.showPosByVal(5)
    linkList.get_length()
    linkList.last_node()
    print("Reversed linked list: ")
    linkList.reverse_linked_list()
