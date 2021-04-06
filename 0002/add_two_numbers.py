# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = tail = None
        extra = 0
        while l1 or l2:
            r = extra
            if l1:
                r += l1.val
                l1 = l1.next
            if l2:
                r += l2.val
                l2 = l2.next
            r1 = r % 10
            extra = int(r / 10)
            if result is None:
                result = tail = ListNode(r1)
            else:
                tail.next = ListNode(r1)
                tail = tail.next
        if extra != 0:
            tail.next = ListNode(1)
        return result


if __name__ == "__main__":
    r = Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
    while r is not None:
        print(r.val, end=' ')
        r = r.next
