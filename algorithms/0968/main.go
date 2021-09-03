package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minCameraCover(root *TreeNode) int {
	var res int
	var postorder func(root *TreeNode) int
	postorder = func(root *TreeNode) int {
		// 0: 无覆盖 1：有摄像头 2：有覆盖
		if root == nil {
			return 2
		}
		left := postorder(root.Left)
		right := postorder(root.Right)
		// handle root
		if left == 2 && right == 2 {
			return 0
		}
		if left == 0 || right == 0 {
			res++
			return 1
		}
		if left == 1 || right == 1 {
			return 2
		}
		return -1
	}
	r := postorder(root)
	if r == 0 {
		res++
	}
	return res
}

func main() {
	fmt.Println(minCameraCover(&TreeNode{0, &TreeNode{0, &TreeNode{0, nil, nil}, &TreeNode{0, nil, nil}}, nil}))
}
