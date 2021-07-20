# Definition for a binary tree node.
import json
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None

        tn = TreeNode()
        if root1 is not None and root2 is not None:
            tn.val = root1.val + root2.val
            tn.left = self.mergeTrees(root1.left, root2.left)
            tn.right = self.mergeTrees(root1.right, root2.right)
        elif root1 is not None:
            tn = root1
        else:
            tn = root2
        return tn


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(5)), TreeNode(3, None, TreeNode(7)))
    t3 = Solution().mergeTrees(t1, t2)
    print(t3.toJSON())
