package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}
	fast, slow := head, head
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
		if fast != nil {
			fast = fast.Next
		}
		if fast == slow {
			break
		}
	}
	if fast == nil {
		return nil
	}
	// reset slow to head
	slow = head
	for slow != fast {
		fast = fast.Next
		slow = slow.Next
	}
	return fast
}

func main() {

}
