class Tree:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
        return root

    if node.value < root.value:  # left
        root.left = insert(root.left, node)

    if node.value > root.value:  # right
        root.right = insert(root.right, node)

    return root


def preOrder(root):  # root --> left --> right
    if root:
        print(root.value, end=' ')
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):  # left --> right --> root
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end=' ')


def InOrder(root):  # left --> root --> right
    if root:
        InOrder(root.left)
        print(root.value, end=' ')
        InOrder(root.right)


def findMinNode(root):  # most left
    size = 1
    if root:
        while root.left:
            root = root.left
            size += 1
        return root.value, size


def findMaxNode(root):  # most right
    size = 1
    if root:
        while root.right:
            root = root.right
            size += 1
        return root.value, size


def deleteNode(root, value):  # ******* important **********
    if root is None:
        return root

    if value < root.value:
        root.left = deleteNode(root.left, value)
    elif value > root.value:
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None:
            # temp = root.right
            # root = None
            # return temp
            root = root.right
            return root

        elif root.right is None:
            # temp = root.left
            # root = None
            # return temp
            root = root.left
            return root

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

print('pre-order(root->left->right):')
preOrder(rt)

print('\n')
print('post-order(left->right->root):')
postOrder(rt)

print('\n')
print('in-order(left->root->right):')
InOrder(rt)

print('\n')
print(f"Min val & size of BST: {findMinNode(rt)}, Max val & size of BST: {findMaxNode(rt)}")

deleteNode(rt, 10)
