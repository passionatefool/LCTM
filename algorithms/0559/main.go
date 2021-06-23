package main

import "fmt"

type Node struct {
	Val      int
	Children []*Node
}

func maxDepth(root *Node) int {
	if root == nil {
		return 0
	}
	depth := 0
	if len(root.Children) > 0 {
		for _, c := range root.Children {
			depth = max(depth, maxDepth(c))
		}
	}
	return depth + 1
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maxDepth(&Node{1, []*Node{&Node{3, []*Node{&Node{5, nil}, &Node{6, nil}}}, &Node{2, nil}, &Node{4, nil}}}))
}
