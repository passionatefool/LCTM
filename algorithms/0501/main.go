package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findMode(root *TreeNode) []int {
	var res []int
	var pre *TreeNode
	count := 0
	max := 0
	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		dfs(root.Left)
		if pre != nil && pre.Val == root.Val {
			count++
		} else {
			count = 1
		}

		if count == max {
			res = append(res, root.Val)
		}
		if count > max {
			res = []int{root.Val}
			max = count
		}
		pre = root
		dfs(root.Right)
	}
	dfs(root)
	return res
}

func main() {
	fmt.Println(findMode(&TreeNode{1, nil, &TreeNode{2, &TreeNode{2, nil, nil}, nil}}))
}
