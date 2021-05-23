package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	var res [][]int
	queue := []*TreeNode{root}
	if root == nil {
		return res
	}
	for level := 0; len(queue) > 0; level++ {
		res = append(res, []int{})
		var next []*TreeNode
		for i := 0; i < len(queue); i++ {
			node := queue[i]
			res[level] = append(res[level], node.Val)
			if node.Left != nil {
				next = append(next, node.Left)
			}
			if node.Right != nil {
				next = append(next, node.Right)
			}
		}
		queue = next
	}
	return res
}

func main() {
	fmt.Println(levelOrder(
		&TreeNode{
			3,
			&TreeNode{9, nil, nil},
			&TreeNode{20, nil, nil},
		},
	),
	)
}
