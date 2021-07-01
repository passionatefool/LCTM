package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 || len(postorder) == 0 {
		return nil
	}

	rootVal := postorder[len(postorder)-1]
	root := &TreeNode{rootVal, nil, nil}

	var cutPoint int
	for i, v := range inorder {
		if v == rootVal {
			cutPoint = i
			break
		}
	}
	inorderLeft, inoderRight := inorder[:cutPoint], inorder[cutPoint+1:]
	postorderLeft, postorderRight := postorder[:len(inorderLeft)], postorder[len(inorderLeft):len(postorder)-1]

	root.Left = buildTree(inorderLeft, postorderLeft)
	root.Right = buildTree(inoderRight, postorderRight)
	return root
}

func main() {
	fmt.Println(buildTree([]int{9, 3, 15, 20, 7}, []int{9, 15, 7, 20, 3}))
}
