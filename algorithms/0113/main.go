package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	var res [][]int
	var path []int
	var dfs func(root *TreeNode, path []int, sum int)
	dfs = func(root *TreeNode, path []int, sum int) {
		if root == nil {
			return
		}
		path = append(path, root.Val)
		if root.Left == nil && root.Right == nil && sum == root.Val {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		dfs(root.Left, path, sum - root.Val)
		dfs(root.Right, path, sum - root.Val)
	}
	dfs(root, path, targetSum)
	return res
}

func main() {
	res := pathSum(
		&TreeNode{
			5,
			&TreeNode{4, &TreeNode{11, &TreeNode{7, nil, nil}, &TreeNode{2, nil, nil}}, nil},
			&TreeNode{8, &TreeNode{13, nil, nil}, &TreeNode{4, &TreeNode{5, nil, nil}, &TreeNode{1, nil, nil}}},
		},
		22,
		)
	fmt.Println(res)
}
