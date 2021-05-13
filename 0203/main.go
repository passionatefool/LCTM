package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// 单独处理头节点的情况
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

// 使用 dummy head 来统一处理头结点的情况
func removeElements2(head *ListNode, val int) *ListNode {
	dummyHead := &ListNode{-1, head}
	pre := dummyHead
	cur := head
	for cur != nil {
		if cur.Val == val {
			pre.Next = cur.Next
		} else {
			pre = cur
		}
		cur = cur.Next
	}
	return dummyHead.Next
}

func main() {
	fmt.Println(removeElements2(
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
