package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	midIndex := len(nums) / 2
	root := &TreeNode{nums[midIndex], nil, nil}
	left := nums[:midIndex]
	right := nums[midIndex+1:]
	root.Left = sortedArrayToBST(left)
	root.Right = sortedArrayToBST(right)
	return root
}

func main() {
	fmt.Println(sortedArrayToBST([]int{-10, -3, 0, 5, 9}))
}
