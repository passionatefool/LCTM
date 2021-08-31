# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nt):
        self.val = x
        self.next = nt


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    n = ListNode(1, ListNode(9, None))
    r = ListNode(4, ListNode(5, n))
    Solution().deleteNode(n)
    while r:
        print(r.val, end=' ')
        r = r.next
