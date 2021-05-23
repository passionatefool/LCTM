# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cur = head
        i = 1
        before = None
        reversed_head, reversed_end = None, None

        while cur is not None:
            if left <= i <= right:
                n = ListNode(cur.val)
                if reversed_head is None:
                    reversed_end = n
                else:
                    n.next = reversed_head
                reversed_head = n
            elif i == right + 1:
                reversed_end.next = cur
            elif i == left - 1:
                before = cur
            cur = cur.next
            i += 1

        if before is None:
            head = reversed_head
        else:
            before.next = reversed_head
        return head


if __name__ == "__main__":
    r = Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
    while r is not None:
        print(r.val, end=" ")
        r = r.next
