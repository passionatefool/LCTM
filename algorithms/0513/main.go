package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findBottomLeftValue(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{root}
	res := 0
	for len(queue) != 0 {
		length := len(queue)
		for i := 0; i < length; i++ {
			cur := queue[0]
			queue = queue[1:]
			if i == 0 {
				res = cur.Val
			}
			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
		}
	}
	return res
}

func main() {
	fmt.Println(findBottomLeftValue(&TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}))
}
