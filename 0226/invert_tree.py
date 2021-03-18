import json


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        Solution.invertTree(self, root.left)
        Solution.invertTree(self, root.right)
        return root


def main():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    s = Solution()
    s.invertTree(root)


if __name__ == "__main__":
    main()
