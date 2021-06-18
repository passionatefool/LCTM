package main

import "fmt"

type Node struct {
	Val      int
	Children []*Node
}

func levelOrder(root *Node) [][]int {
	var res [][]int
	if root == nil {
		return res
	}
	queue := []*Node{root}
	for len(queue) != 0 {
		length := len(queue)
		var subList []int
		for i := 0; i < length; i++ {
			cur := queue[0]
			queue = queue[1:]
			subList = append(subList, cur.Val)
			for _, c := range cur.Children {
				queue = append(queue, c)
			}
		}
		res = append(res, subList)
	}
	return res
}

func main() {
	fmt.Println(
		levelOrder(
			&Node{1, []*Node{
				&Node{3, []*Node{&Node{5, []*Node{}}, &Node{6, []*Node{}}}},
				&Node{2, []*Node{}},
				&Node{4, []*Node{}}}},
		),
	)
}
