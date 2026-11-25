class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.head = None

    def Insert(self, val):
        if self.head is None:
            self.head = TreeNode(val)
            return
        node = self.head
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    return
                node = node.right

    def IsSameTree(self, p):
        return 1 if same(self.head, p.head) else 0


def same(a, b):
    if a is None or b is None:
        return a is b
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)


def read_tree():
    n = int(input())
    tree = Tree()
    for x in input().split()[:n]:
        tree.Insert(int(x))
    return tree


first = read_tree()
second = read_tree()
print(first.IsSameTree(second))
