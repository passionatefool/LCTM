package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil && root2 == nil {
		return nil
	}
	if root1 != nil && root2 != nil {
		return &TreeNode{
			root2.Val + root1.Val,
			mergeTrees(root1.Left, root2.Left),
			mergeTrees(root1.Right, root2.Right),
		}
	} else {
		if root1 == nil && root2 != nil {
			return &TreeNode{root2.Val, mergeTrees(nil, root2.Left), mergeTrees(nil, root2.Right)}
		} else {
			return &TreeNode{root1.Val, mergeTrees(root1.Left, nil), mergeTrees(root1.Right, nil)}
		}
	}
}

func main() {
	fmt.Println()
}
