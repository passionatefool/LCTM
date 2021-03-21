package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	// 终止条件：节点为空或节点只有一个值
	// 返回值：已经交换好的链表
	// 本级递归逻辑： 反转
	if head == nil || head.Next == nil {
		return head
	}
	tmpNext := head.Next
	// 反转后的新头
	newHead := reverseList(tmpNext)
	tmpNext.Next = head
	head.Next = nil
	return newHead
}
func main() {
	fmt.Println(reverseList(&ListNode{1, &ListNode{2, &ListNode{3, nil}}}))
}
