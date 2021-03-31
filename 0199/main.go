package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		length := len(queue)
		res = append(res, queue[length - 1].Val)
		for i := 0; i < length; i++ {
			node := queue[0]
			queue = queue[1:]
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return res
}

func main() {
	fmt.Println(rightSideView(
		&TreeNode{
			1,
			&TreeNode{2, nil, &TreeNode{5, nil, nil}},
			&TreeNode{3, nil, &TreeNode{4, nil, nil}}}))
}
