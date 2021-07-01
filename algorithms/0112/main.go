package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	res := false
	if root == nil {
		return false
	}
	var dfs func(root *TreeNode, sum int)
	dfs = func(root *TreeNode, sum int) {
		if root == nil {
			return
		}
		if root.Left == nil && root.Right == nil && sum == root.Val {
			res = true
		}
		dfs(root.Left, sum - root.Val)
		dfs(root.Right, sum - root.Val)
	}
	dfs(root, targetSum)
	return res
}

func main() {
	fmt.Println(hasPathSum(&TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{3, nil, nil}}, 5))

}
