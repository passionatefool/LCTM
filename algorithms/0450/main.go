package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func del(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	if root.Right == nil {
		return root.Left
	}
	tmp := root.Right
	for tmp.Left != nil {
		tmp = tmp.Left
	}
	tmp.Left = root.Left
	return root.Right
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	tmp := root
	var pre *TreeNode
	if root == nil {
		return root
	}
	for tmp != nil {
		if tmp.Val == key {
			break
		}
		pre = tmp
		if tmp.Val > key {
			tmp = tmp.Left
		} else {
			tmp = tmp.Right
		}
	}
	if pre == nil {
		return del(tmp)
	}
	if pre.Left != nil && pre.Left.Val == key {
		pre.Left = del(tmp)
	}
	if pre.Right != nil && pre.Right.Val == key {
		pre.Right = del(tmp)
	}
	return root
}

func main() {
	fmt.Println()
}
