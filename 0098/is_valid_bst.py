# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        self.rangeTree(root, result)
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
        return True

    def rangeTree(self, root: TreeNode, result: List[int]):
        if root is None:
            return
        self.rangeTree(root.left, result)
        result.append(root.val)
        self.rangeTree(root.right, result)


if __name__ == "__main__":
    s = Solution()
    print(s.isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))))
