package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
	maxVal := 0
	maxIndex := 0
	if len(nums) == 0 {
		return nil
	}
	for i, v := range nums {
		if i==0 || v > maxVal {
			maxVal = v
			maxIndex = i
		}
	}
	leftNums, rightNums := nums[:maxIndex], nums[maxIndex+1:]
	root := &TreeNode{maxVal, constructMaximumBinaryTree(leftNums), constructMaximumBinaryTree(rightNums)}
	return root
}

func main() {
	fmt.Println(constructMaximumBinaryTree([]int{3, 2, 1, 6, 0, 5}))
}
