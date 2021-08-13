package main;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        merge(l1,l2);
        return l1;
    }

    private void merge(ListNode l1, ListNode l2) {
        while (l1 != null) {
            if (l2 != null) {
                l1.val = l1.val + l2.val;
                l2 = l2.next;
                if (l2 != null && l1.next == null) {
                    l1.next = new ListNode();
                }
            }
            if (l1.val >= 10) {
                if (l1.next == null) {
                    l1.next = new ListNode();
                }
                l1.next.val = l1.next.val + l1.val / 10;
                l1.val = l1.val % 10;
            }
            l1 = l1.next;
        }
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}