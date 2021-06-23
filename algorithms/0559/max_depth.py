# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0
        if len(root.children) == 0:
            return 1

        nm = 0
        for r in root.children:
            n = self.maxDepth(r)
            if n > nm:
                nm = n
        return 1 + nm
