import sys


class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return TreeNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def preorder(node, out):
    if node is None:
        return
    out.append(node.key)
    preorder(node.left, out)
    preorder(node.right, out)


def build(lines):
    root = None
    for line in reversed(lines):
        for ch in line:
            root = insert(root, ch)
    out = []
    preorder(root, out)
    return "".join(out)


def main():
    result = []
    lines = []
    for raw in sys.stdin.read().split("\n"):
        line = raw.strip()
        if not line:
            continue
        if line[0] in "*$":
            result.append(build(lines))
            lines = []
            if line[0] == "*":
                break
        else:
            lines.append(line)
    sys.stdout.write("\n".join(result) + "\n")


main()
