package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}
	rootVal := preorder[0]
	root := &TreeNode{rootVal, nil, nil}

	var cutPoint int
	for i, v := range inorder {
		if v == rootVal {
			cutPoint = i
			break
		}
	}
	preorderLeft, preorderRight := preorder[1:cutPoint+1], preorder[cutPoint+1:]
	inorderLeft, inorderRight := inorder[:cutPoint], inorder[cutPoint+1:]

	root.Left = buildTree(preorderLeft, inorderLeft)
	root.Right = buildTree(preorderRight, inorderRight)
	return root
}

func main() {
	fmt.Println(buildTree([]int{3, 9, 20, 15, 7}, []int{9, 3, 15, 20, 7}))
}
