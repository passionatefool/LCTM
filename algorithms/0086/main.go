package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	big, small := &ListNode{0, nil}, &ListNode{0, nil}
	dummyBig, dummySmall := big, small
	for head != nil {
		if head.Val < x {
			small.Next = head
			small = small.Next
		} else {
			big.Next = head
			big = big.Next
		}
		head = head.Next
	}
	small.Next = dummyBig.Next
	big.Next = nil
	return dummySmall.Next
}

func main() {
	res := partition(&ListNode{1, &ListNode{4, &ListNode{3, &ListNode{2, &ListNode{5, &ListNode{2, nil}}}}}}, 3)
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}
