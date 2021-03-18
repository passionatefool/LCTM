package main

import "fmt"

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return root
    }
    invertTree(root.Left)
    invertTree(root.Right)

    root.Left, root.Right = root.Right, root.Left
    return root
}

func main()  {
	root := TreeNode{
	    4,
	    &TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}},
	    &TreeNode{7, &TreeNode{6, nil, nil}, &TreeNode{9, nil, nil}},
	}
	fmt.Println(invertTree(&root))
}
