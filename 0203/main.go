package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	for head != nil && head.Val == val {
		head = head.Next
	}
	p := head
	for p != nil && p.Next != nil {
		if p.Next.Val == val {
			p.Next = p.Next.Next
		} else {
			p = p.Next
		}
	}
	return head
}

func main() {
	fmt.Println(removeElements(
		&ListNode{
			1, &ListNode{
				2, &ListNode{
					6, &ListNode{
						3, &ListNode{
							4, &ListNode{
								5, &ListNode{
									6, nil,
								},
							},
						},
					},
				},
			},
		},
		6,
	))
}
