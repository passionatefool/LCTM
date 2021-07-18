# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, root: Node, depth: int, res: List[List[int]]):
        if root is None:
            return
        if len(res) <= depth:
            res.append([])
        cur = res[depth]
        cur.append(root.val)
        for c in root.children:
            self.helper(c, depth + 1, res)
