package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	var check func(l, r *TreeNode) bool
	check = func(l, r *TreeNode) bool {
		if l == nil && r == nil {
			return true
		}
		if l == nil || r == nil {
			return false
		}
		if l.Val != r.Val {
			return false
		}
		return check(l.Left, r.Right) && check(l.Right, r.Left)
	}
	return check(root, root)
}

func main() {
	fmt.Println(isSymmetric(
		&TreeNode{
			1,
			&TreeNode{2, &TreeNode{3, nil, nil}, &TreeNode{4, nil, nil}},
			&TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{3, nil, nil}},
		},
	))
}
