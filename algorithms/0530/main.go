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

func getMinimumDifference(root *TreeNode) int {
	res := math.MaxInt64
	var pre *TreeNode
	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		dfs(root.Left)
		if pre != nil {
			tmp := root.Val - pre.Val
			if tmp < res && pre != nil {
				res = tmp
			}
		}
		pre = root
		dfs(root.Right)
	}
	dfs(root)
	return res
}

func main() {
	fmt.Println(getMinimumDifference(&TreeNode{1, nil, &TreeNode{3, &TreeNode{2, nil, nil}, nil}}))
}
