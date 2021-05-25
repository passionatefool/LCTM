package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
	res := []int{}
	var f func(node *TreeNode)
	f = func(root *TreeNode) {
		if root == nil {
			return
		}
		res = append(res, root.Val)
		f(root.Left)
		f(root.Right)
	}
	f(root)
	return res
}
