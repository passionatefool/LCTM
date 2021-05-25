# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 1
        cur = head
        odd_tail = even_tail = None
        while cur is not None:
            if i % 2 == 1:
                if odd_tail is None:
                    odd_tail = cur
                else:
                    tmp = odd_tail.next
                    cur_next = cur.next
                    odd_tail.next = cur
                    cur.next = tmp
                    odd_tail = cur
                    even_tail.next = cur_next
                    cur = even_tail
            else:
                if even_tail is None:
                    even_tail = cur
                    odd_tail.next = even_tail
                else:
                    even_tail = cur

            cur = cur.next
            i += 1
        return head


if __name__ == "__main__":
    n = Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while n is not None:
        print(n.val, end=" ")
        n = n.next
