package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	var pre *ListNode = nil
	fast, slow := head, head

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	for slow != nil {
		tmp := slow.Next
		slow.Next = pre
		pre = slow
		slow = tmp
	}
	for head != nil && pre != nil {
		if head.Val != pre.Val {
			return false
		}
		head = head.Next
		pre = pre.Next
	}
	return true
}

func main() {
	fmt.Println(isPalindrome(&ListNode{1, &ListNode{2, &ListNode{2, &ListNode{1, nil}}}}))

}
