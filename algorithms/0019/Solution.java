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
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int len = getLen(head);
        if (len == n) {
            return head.next;
        }
        handle(head, len - n + 1);
        return head;
    }

    private void handle(ListNode head, int n) {
        for (int i = 0; i < n - 2; i++) {
            head = head.next;
        }
        ListNode next = head.next;
        head.next = next.next;
    }

    private int getLen(ListNode head) {
        int n = 0;
        while (head != null) {
            head = head.next;
            n++;
        }
        return n;
    }

    public void getNode(ListNode listNode, int i) {
        while (i >= 1) {
            if (i == 1) {
                listNode.next = new ListNode(i);
            } else {
                listNode.next = new ListNode(i, new ListNode());
            }
            listNode = listNode.next;
            i--;
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