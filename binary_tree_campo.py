"""Assessment 3.3 - Diagram 1: Binary Tree (CAMPO)
Algorithm 1: BFS (queue)    Algorithm 2: DFS preorder (stack)

        C
       / \
      A   M
     / \
    P   O
"""
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    result = []
    q = deque([root])                      # steps 2-3
    while q:                               # step 4
        current = q.popleft()              # step 5
        result.append(current.value)       # step 6
        if current.left:                   # step 7
            q.append(current.left)
        if current.right:                  # step 8
            q.append(current.right)
    return result


def dfs(root):
    result = []
    stack = [root]                         # steps 2-3
    while stack:                           # step 4
        current = stack.pop()              # step 5
        result.append(current.value)       # step 6
        if current.right:                  # step 7 (right pushed first)
            stack.append(current.right)
        if current.left:                   # step 8 (left popped first)
            stack.append(current.left)
    return result


if __name__ == "__main__":
    root = Node("C", Node("A", Node("P"), Node("O")), Node("M"))
    print("BFS (Binary Tree):", " - ".join(bfs(root)))
    print("DFS (Binary Tree):", " - ".join(dfs(root)))
