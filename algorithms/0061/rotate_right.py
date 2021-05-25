# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        k %= count
        if k == 0:
            return head

        k = -k
        cur = cur1 = tail = before = head

        while cur:
            if k >= 0:
                before = cur1
                cur1 = cur1.next
            k += 1
            cur = cur.next
            if cur is not None:
                tail = cur

        if before is None:
            return cur1
        tail.next = head
        before.next = None
        return cur1


if __name__ == "__main__":
    r = Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    while r:
        print(r.val, end=" ")
        r = r.next
