# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_depth, right_depth = self.depth(root.left), self.depth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))


if __name__ == "__main__":
    s = Solution()
    print(s.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))
