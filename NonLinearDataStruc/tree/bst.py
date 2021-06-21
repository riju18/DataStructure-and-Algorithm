class Tree:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
        return root

    if node.value < root.value:
        root.left = insert(root.left, node)

    if node.value > root.value:
        root.right = insert(root.right, node)

    return root


def preOrder(root):
    if root:
        print(root.value, end=' ')
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end=' ')


def InOrder(root):
    if root:
        postOrder(root.left)
        print(root.value, end=' ')
        postOrder(root.right)


def findMinNode(root):
    if root:
        while root.left is not None:
            root = root.left
        return root.value


def findMaxNode(root):
    if root:
        while root.right is not None:
            root = root.right
        return root.value


def deleteNode(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = deleteNode(root.left, value)
    if value > root.value:
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        else:
            temp = findMinNode(root.right)
            root.value = temp
            root.right = deleteNode(root.right, temp)

        return root


rt = Tree(100)

insert(rt, Tree(21))
insert(rt, Tree(50))
insert(rt, Tree(10))
insert(rt, Tree(101))
insert(rt, Tree(150))
insert(rt, Tree(99))
insert(rt, Tree(220))
insert(rt, Tree(103))

print('pre-order(root->left->right): \n')
preOrder(rt)

print('\n')
print('post-order(left->right->root): \n')
postOrder(rt)

print('\n')
print('in-order(left->root->right): \n')
InOrder(rt)

print('\n', 'minimum value of BST: ', findMinNode(rt), '\n')
print('\n', 'maximum value of BST: ', findMaxNode(rt), '\n')

deleteNode(rt, 10)
print('\n')
print('post-order(left->right->root): \n')
postOrder(rt)
