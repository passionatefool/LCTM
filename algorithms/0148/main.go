package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	// 找到中点进行断链
	slow := head
	fast := head

	for fast != nil && fast.Next != nil && fast.Next.Next != nil{
		slow = slow.Next
		fast = fast.Next.Next
	}

	secondListHead := slow.Next
	slow.Next = nil

	// 递归排序两部分
	firstList := sortList(head)
	secondList := sortList(secondListHead)

	// 合并
	return merge(firstList, secondList)
}

func merge(firstList *ListNode, secondList *ListNode) *ListNode {
	dummyHead := &ListNode{}
	dummy := dummyHead
	for firstList != nil && secondList != nil {
		if firstList.Val <= secondList.Val {
			dummy.Next = firstList
			firstList = firstList.Next
			dummy = dummy.Next
		} else {
			dummy.Next = secondList
			secondList = secondList.Next
			dummy = dummy.Next
		}
	}

	if firstList != nil {
		dummy.Next = firstList
	} else if secondList != nil {
		dummy.Next = secondList
	}
	return dummyHead.Next
}

func main() {
	sorted := sortList(&ListNode{4, &ListNode{2, &ListNode{1, &ListNode{3, nil}}}})
	for sorted != nil {
		fmt.Println(sorted.Val)
		sorted = sorted.Next
	}
}
