# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []
        self.cur = 0
        self.max = 0
        self.prev = None

    def findMode(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.result

    def dfs(self, root: TreeNode):
        if root is None:
            return
        self.dfs(root.left)
        if root.val != self.prev:
            self.cur = 1
        else:
            self.cur += 1
        if self.cur == self.max:
            self.result.append(root.val)
        elif self.cur > self.max:
            self.max = self.cur
            self.result = [root.val]
        self.prev = root.val
        self.dfs(root.right)


if __name__ == "__main__":
    print(Solution().findMode(TreeNode(1, None, TreeNode(2, TreeNode(2)))))
