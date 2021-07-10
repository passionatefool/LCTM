# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        h1 = h2 = head
        while h2.next and h2.next.next:
            h1 = h1.next
            h2 = h2.next.next

        cur = h1.next
        h1.next = None
        h3 = None
        while cur:
            next = cur.next
            cur.next = h3
            h3 = cur
            cur = next
        i, j = head, h3
        while j:
            n1, n2 = i.next, j.next
            i.next = j
            j.next = n1
            i, j = n1, n2


if __name__ == "__main__":
    hh = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().reorderList(hh))
    while hh:
        print(hh.val, end=" ")
        hh = hh.next
