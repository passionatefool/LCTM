package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) []int {
	var res []int
	if root == nil {
		return res
	}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		length := len(queue)
		max := math.MinInt32
		for i := 0; i < length; i++ {
			cur := queue[0]
			queue = queue[1:]
			if cur.Val > max {
				max = cur.Val
			}
			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
		}
		res = append(res, max)
	}
	return res
}

func main() {
	fmt.Println(largestValues(&TreeNode{
		1,
		&TreeNode{3, &TreeNode{5, nil, nil}, &TreeNode{3, nil, nil}},
		&TreeNode{2, nil, &TreeNode{9, nil, nil}},
	}))
}
