# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        self.handleLevel(root, 1, [])
        return root

    def handleLevel(self, root: Node, depth: int, res: List['Node']):
        if root is None:
            return
        if len(res) < depth:
            res.append(root)
        else:
            res[depth - 1].next = root
            res[depth - 1] = root

        depth = depth + 1
        self.handleLevel(root.left, depth, res)
        self.handleLevel(root.right, depth, res)
