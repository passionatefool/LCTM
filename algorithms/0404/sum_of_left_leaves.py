# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left, val = root.left, 0
        if left is not None and left.left is None and left.right is None:
            val = left.val
        return val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


if __name__ == "__main__":
    print(Solution().sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
