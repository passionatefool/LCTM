# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1, n)

    def generate(self, start, end: int) -> List[TreeNode]:
        if start > end:
            return [None]
        res = []
        for i in range(start, end+1):
            left = self.generate(start, i - 1)
            right = self.generate(i + 1, end)

            for l in left:
                for r in right:
                    root = TreeNode(i, l, r)
                    res.append(root)
        return res


if __name__ == "__main__":
    print(Solution().generateTrees(3))
