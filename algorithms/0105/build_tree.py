from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        val = preorder[0]
        index = inorder.index(val)

        return TreeNode(val, self.buildTree(preorder[1:index + 1], inorder[:index]),
                        self.buildTree(preorder[index + 1:], inorder[index + 1:]))


if __name__ == "__main__":
    tree = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    s = [tree]
    while len(s) > 0:
        tn = s.pop()
        print(tn.val, end=' ')
        if tn.right:
            s.append(tn.right)
        if tn.left:
            s.append(tn.left)
