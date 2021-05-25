package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) (head *ListNode) {
	var res *ListNode
	tail := 0
	for l1 != nil || l2 != nil {
		n1, n2 := 0, 0
		if l1 != nil {
			n1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			n2 = l2.Val
			l2 = l2.Next
		}
		sum := (n1 + n2 + tail)%10
		tail = (n1 + n2 + tail)/10
		if head == nil {
			head = &ListNode{sum, nil}
			res = head
		} else {
			res.Next = &ListNode{sum, nil}
			res = res.Next
		}
	}
	if tail > 0 {
		res.Next = &ListNode{tail, nil}
	}
	return head
}
func main() {

}
