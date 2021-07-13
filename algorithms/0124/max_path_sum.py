# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_helper(root)
        return int(self.result)

    def max_helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = max(self.max_helper(root.left), 0)
        right = max(self.max_helper(root.right), 0)

        self.result = max(left + right + root.val, self.result)
        return max(left, right) + root.val
