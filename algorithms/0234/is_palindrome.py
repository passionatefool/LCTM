# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val

        fast, slow, slow_next = head, head, head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            pre = slow
            slow = slow_next
            slow_next = slow.next
            slow.next = pre

        # odd
        if fast.next is None:
            slow = slow.next
        while slow_next:
            if slow.val != slow_next.val:
                return False
            slow, slow_next = slow.next, slow_next.next
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
