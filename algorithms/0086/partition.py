# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        nh1, nh2, l1, l2 = None, None, None, None
        while head:
            nl = ListNode(head.val)
            if head.val < x:
                if l1 is None:
                    nh1 = l1 = nl
                else:
                    l1.next = nl
                    l1 = nl
            else:
                if l2 is None:
                    nh2 = l2 = nl
                else:
                    l2.next = nl
                    l2 = nl
            head = head.next

        if l1 is None:
            return nh2
        l1.next = nh2
        return nh1


if __name__ == "__main__":
    h = Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3)
    while h:
        print(h.val, end=" ")
        h = h.next
