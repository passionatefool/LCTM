package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {
	res := math.MinInt32
	var getMax func(root *TreeNode) int
	getMax = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := max(0, getMax(root.Left))
		right := max(0, getMax(root.Right))
		res = max(res, left+right+root.Val)
		return max(left, right) + root.Val
	}
	getMax(root)
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maxPathSum(&TreeNode{-10, &TreeNode{9, nil, nil}, &TreeNode{20, &TreeNode{15, nil, nil}, &TreeNode{7, nil, nil}}}))
}
