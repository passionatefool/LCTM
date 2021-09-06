# Definition for a binary tree node.
import json
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        node = TreeNode(postorder.pop())
        i = inorder.index(node.val)
        node.right = self.buildTree(inorder[i + 1:], postorder)
        node.left = self.buildTree(inorder[:i], postorder)
        return node


if __name__ == "__main__":
    node = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(node.toJSON())
