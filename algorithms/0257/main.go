package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePaths(root *TreeNode) []string {
	var res []string
	var f func(root *TreeNode, s string)
	f = func(root *TreeNode, s string) {
		if root.Left == nil && root.Right == nil {
			res = append(res, s + strconv.Itoa(root.Val))
			return
		}
		s = s + strconv.Itoa(root.Val) + "->"
		if root.Left != nil {
			f(root.Left, s)
		}
		if root.Right != nil {
			f(root.Right, s)
		}
	}
	f(root, "")
	return res
}

func main() {
	fmt.Println(binaryTreePaths(&TreeNode{1, &TreeNode{2, nil, &TreeNode{5, nil, nil}}, &TreeNode{3, nil, nil}}))
}
