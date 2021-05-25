# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        i = 1
        before = None
        pre = None
        while cur is not None:
            if i % 2 == 1:
                before = cur
            else:
                n = cur.next
                cur.next = before
                before.next = n
                if pre is None:
                    pre = before
                    head = cur
                else:
                    pre.next = cur
                    pre = before
                cur = before

            cur = cur.next
            i += 1

        return head


if __name__ == "__main__":
    n = Solution()
    r = n.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    while r is not None:
        print(r.val, end=' ')
        r = r.next
