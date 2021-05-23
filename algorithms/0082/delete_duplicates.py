# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur, pre, nh = head, None, None
        count, tmp = 0, None
        while cur is not None:
            if tmp is None:
                count, tmp = 1, cur
            elif cur.val == tmp.val:
                count += 1
            else:
                if count == 1:
                    tmp.next = None
                    if pre is None:
                        nh = pre = tmp
                    else:
                        pre.next = tmp
                        pre = tmp
                if cur.next is None:
                    if pre is None:
                        nh = pre = cur
                    else:
                        pre.next = cur
                else:
                    count, tmp = 1, cur
            cur = cur.next
        return nh


if __name__ == "__main__":
    nh = Solution().deleteDuplicates(
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
    while nh is not None:
        print(nh.val, end=" ")
        nh = nh.next
