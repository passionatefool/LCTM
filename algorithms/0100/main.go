package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if (p == nil && q != nil) || (p != nil && q == nil) {
		return false
	}
	if p == nil && q == nil {
		return true
	}
	if p != nil && q != nil {
		if p.Val == q.Val {
			return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
		} else {
			return false
		}
	}
	return false
}

// 更好的写法
func isSameTree2(p *TreeNode, q *TreeNode) bool {
	switch {
	case p == nil && q == nil:
		return true
	case p == nil || q == nil:
		fallthrough
	case p.Val != q.Val:
		return false
	}
	return isSameTree2(p.Left, q.Left) && isSameTree2(p.Right, q.Right)
}

func main() {
	fmt.Println(isSameTree(
		&TreeNode{1,
			&TreeNode{2, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{1,
			&TreeNode{2, nil, nil},
			&TreeNode{3, nil, nil}}))
}
