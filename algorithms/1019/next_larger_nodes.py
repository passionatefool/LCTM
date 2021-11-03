# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        stack, res = [], [0] * len(l)
        for i in range(len(l)):
            while stack and l[stack[-1]] < l[i]:
                res[stack.pop()] = l[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    print(Solution().nextLargerNodes(ListNode(2, ListNode(1, ListNode(5)))))
