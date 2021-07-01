# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == "__main__":
    print(Solution().hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
