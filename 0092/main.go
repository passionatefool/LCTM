package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseLink(head *ListNode) *ListNode {
	// 同 206：反转链表
	var newHead *ListNode
	cur := head
	for cur != nil {
		next := cur.Next
		cur.Next = newHead
		newHead = cur
		cur = next
	}
	return newHead
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	// 定义五个节点：dummyNode，preNode, leftNode, rightNode, postNode
	var dummyNode = &ListNode{Val: -1}
	dummyNode.Next = head
	preNode := dummyNode
	for i := 0; i < left-1; i++ {
		preNode = preNode.Next
	}

	leftNode := preNode.Next

	rightNode := preNode
	for i := 0; i < right-left+1; i++ {
		rightNode = rightNode.Next
	}

	postNode := rightNode.Next

	// 反转前需要断开原来链接
	preNode.Next = nil
	rightNode.Next = nil

	// 进行子序列反转
	newHead := reverseLink(leftNode)

	// 反转后接回链接
	preNode.Next = newHead
	leftNode.Next = postNode

	return dummyNode.Next
}

func main() {
	fmt.Println(
		reverseBetween(
			&ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}},
			2, 4,
		),
	)
}
