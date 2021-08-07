# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        middle = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(middle)
        res = tmp = ListNode(0)
        while left and right:
            if left.val < right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        tmp.next = left if left else right
        return res.next


if __name__ == "__main__":
    res = Solution().sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))
    while res:
        print(res.val, end=' ')
        res = res.next
