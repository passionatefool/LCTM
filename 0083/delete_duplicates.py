# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur is not None:
            cn = cur.next
            cur.next = None
            if pre is None:
                pre = cur
            elif pre.val != cur.val:
                pre.next = cur
                pre = cur
            cur = cn
        return head


if __name__ == "__main__":
    nh = Solution().deleteDuplicates(
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
    while nh is not None:
        print(nh.val, end=" ")
        nh = nh.next
