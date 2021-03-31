package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	res := [][]int{}
	if root == nil {
		return res
	}
	queue := []*TreeNode{root}
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
		if level % 2 == 1 {
			for i, j := 0, len(res[level])-1; i < j; i, j = i+1, j-1 {
				res[level][i], res[level][j] = res[level][j], res[level][i]
			}
		}
	}
	return res
}

func main() {

}
