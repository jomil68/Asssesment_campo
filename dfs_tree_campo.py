"""Assessment 3.6 - DFS Methods in Tree (CAMPO)
Three DFS traversals: Preorder, Inorder, Postorder
(each in a recursive version and an iterative/stack version)

        C
       / \
      A   M
     / \
    P   O
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# ---------- Recursive versions ----------
def preorder(node, result=None):            # Root -> Left -> Right
    if result is None:
        result = []
    if node:
        result.append(node.value)           # visit root
        preorder(node.left, result)         # go left
        preorder(node.right, result)        # go right
    return result


def inorder(node, result=None):             # Left -> Root -> Right
    if result is None:
        result = []
    if node:
        inorder(node.left, result)          # go left
        result.append(node.value)           # visit root
        inorder(node.right, result)         # go right
    return result


def postorder(node, result=None):           # Left -> Right -> Root
    if result is None:
        result = []
    if node:
        postorder(node.left, result)        # go left
        postorder(node.right, result)       # go right
        result.append(node.value)           # visit root
    return result


# ---------- Iterative versions (using a stack) ----------
def preorder_iterative(root):
    result, stack = [], [root] if root else []
    while stack:
        current = stack.pop()
        result.append(current.value)
        if current.right:                   # right pushed first
            stack.append(current.right)
        if current.left:                    # left popped first
            stack.append(current.left)
    return result


def inorder_iterative(root):
    result, stack, current = [], [], root
    while current or stack:
        while current:                      # go as far left as possible
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)        # visit
        current = current.right             # then go right
    return result


def postorder_iterative(root):
    result, stack = [], [root] if root else []
    while stack:                             # Root -> Right -> Left, then reverse
        current = stack.pop()
        result.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return result[::-1]


if __name__ == "__main__":
    root = Node("C", Node("A", Node("P"), Node("O")), Node("M"))

    print("DFS Methods in Tree")
    print("-" * 40)
    print("Preorder  (Root-Left-Right):", " - ".join(preorder(root)))
    print("Inorder   (Left-Root-Right):", " - ".join(inorder(root)))
    print("Postorder (Left-Right-Root):", " - ".join(postorder(root)))
    print("-" * 40)
    print("Iterative Preorder :", " - ".join(preorder_iterative(root)))
    print("Iterative Inorder  :", " - ".join(inorder_iterative(root)))
    print("Iterative Postorder:", " - ".join(postorder_iterative(root)))
