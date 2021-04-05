package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	cur := head
	for cur.Next != nil {
		if cur.Next.Val == cur.Val {
			next := cur.Next.Next
			cur.Next = next
		} else {
			cur = cur.Next
		}
	}
	return head
}

func main() {
	res := deleteDuplicates(&ListNode{1, &ListNode{1, &ListNode{2, nil}}})
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}
