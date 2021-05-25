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

func isValidBST(root *TreeNode) bool {
	return isBST(root, math.MinInt64, math.MaxInt64)

}

func isBST(root *TreeNode, low, high int) bool {
	if root == nil {
		return true
	}
	if root.Val <= low || root.Val >= high {
		return false
	}
	return isBST(root.Left, low, root.Val) && isBST(root.Right, root.Val, high)
}

func main() {
	fmt.Println(isValidBST(&TreeNode{
		2,
		&TreeNode{1, nil, nil},
		&TreeNode{3, nil, nil},
	}))

}
