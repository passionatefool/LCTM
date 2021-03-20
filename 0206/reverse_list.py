# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head is not None:
            n = head.next
            head.next = pre
            pre = head
            head = n
        return pre


if __name__ == "__main__":
    n = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while n is not None:
        print(n.val, end=" ")
        n = n.next
