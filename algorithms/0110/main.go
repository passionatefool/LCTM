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


func getHigh(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + max(getHigh(root.Left), getHigh(root.Right))
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	leftHigh := getHigh(root.Left)
	rightHigh := getHigh(root.Right)
	if math.Abs(float64(leftHigh - rightHigh)) > 1 {
		return false
	}
	return isBalanced(root.Left) && isBalanced(root.Right)
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(isBalanced(&TreeNode{
		3,
		&TreeNode{9, nil, nil},
		&TreeNode{20, &TreeNode{15, nil, nil}, &TreeNode{7, nil, nil}},
	}))
}
