package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	var res [][]int
	if root == nil {
		return res
	}
	queue := []*TreeNode{root}

	for len(queue) != 0 {
		length := len(queue)
		var subList []int
		for i := 0; i < length; i++ {
			cur := queue[0]
			queue = queue[1:]
			subList = append(subList, cur.Val)
			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
		}
		res = append(res, subList)
	}
	// reverse
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}

func main() {
	t := TreeNode{3, &TreeNode{9, nil, nil}, &TreeNode{20, &TreeNode{15, nil, nil}, &TreeNode{7, nil, nil}}}
	fmt.Println(levelOrderBottom(&t))
}
