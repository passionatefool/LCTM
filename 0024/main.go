package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	// 终止条件： 链表为空或只有一个元素
	// 返回值：已经两两交换的链表
	// 本级递归逻辑：进行两两交换
	if head == nil || head.Next == nil {
		return head
	}
	tmpNext := head.Next
	// 进行两两交换，返回值为已经交换好的链表
	head.Next = swapPairs(tmpNext.Next)
	tmpNext.Next = head
	// 返回已处理好的链表
	return tmpNext
}

func main() {
	fmt.Println(swapPairs(&ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}))
}
