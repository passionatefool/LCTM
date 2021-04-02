package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head
	}
	length := 1
	cur := head
	for cur.Next != nil {
		length ++
		cur = cur.Next
	}

	k = k % length
	if k == 0 {
		return head
	}

	cur.Next = head

	cur = head
	for i := 1; i < length - k; i++ {
		cur = cur.Next
	}
	res := cur.Next
	cur.Next = nil
	return res
}

func main() {
	res := rotateRight(&ListNode{0, &ListNode{1, &ListNode{2, nil}}}, 4)
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}
