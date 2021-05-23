# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = Solution.maxDepth(self, root.left) + 1
        right_depth = Solution.maxDepth(self, root.right) + 1

        return max(left_depth, right_depth)


def main():
    s = Solution()
    print(s.maxDepth(TreeNode(1, None, TreeNode(2))))


if __name__ == "__main__":
    main()
