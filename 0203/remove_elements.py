# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = None
        cur = None
        c = head
        while c is not None:
            if c.val != val:
                if result is None:
                    cur = ListNode(c.val)
                    result = cur
                else:
                    cur.next = ListNode(c.val)
                    cur = cur.next
            c = c.next

        return result
