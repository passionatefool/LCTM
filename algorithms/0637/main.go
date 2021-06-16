package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	var res []float64
	if root == nil {
		return res
	}
	queue := []*TreeNode{root}
	for len(queue) != 0 {
		length := len(queue)
		sum := 0
		i := 0
		for ; i < length; i++ {
			cur := queue[0]
			queue = queue[1:]
			sum += cur.Val
			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
		}
		res = append(res, float64(sum)/float64(i))
	}
	return res
}

func main() {
	fmt.Println(averageOfLevels(&TreeNode{3, &TreeNode{9, nil, nil}, &TreeNode{20, &TreeNode{15, nil, nil}, &TreeNode{7, nil, nil}}}))
}
