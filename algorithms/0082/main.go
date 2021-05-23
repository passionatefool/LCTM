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
	dummy := &ListNode{0, head}
	cur := dummy
	for cur.Next != nil && cur.Next.Next != nil {
		val := cur.Next.Val
		if cur.Next.Val == cur.Next.Next.Val {
			for cur.Next != nil && cur.Next.Val == val {
				cur.Next = cur.Next.Next
			}
		} else {
			cur = cur.Next
		}
	}

	return dummy.Next
}

func main() {
	res := deleteDuplicates(
		&ListNode{1, &ListNode{1, &ListNode{1,
			&ListNode{2, &ListNode{3, nil}}}}},
	)
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}
