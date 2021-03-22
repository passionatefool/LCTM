class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i, j = 0, 0 - n
        cur = cur2 = head
        pre = None
        while cur is not None:
            if j >= 0:
                pre = cur2
                cur2 = cur2.next

            cur = cur.next
            i += 1
            j += 1

        if pre is None:
            return cur2.next
        pre.next = cur2.next
        return head


if __name__ == "__main__":
    r = Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    while r is not None:
        print(r.val, end=' ')
        r = r.next

    r = Solution().removeNthFromEnd(ListNode(1), 1)
    while r is not None:
        print(r.val, end=' ')
        r = r.next
