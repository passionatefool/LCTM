package main

import "fmt"

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

// 使用队列层次优先遍历
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	queue := []*Node{root}
	for len(queue) > 0 {
		length := len(queue)
		for i := 0; i < length; i++ {
			cur := queue[0]
			if length - i - 1 > 0 {
				cur.Next = queue[1]
			} else {
				cur.Next = nil
			}
			queue = queue[1:]

			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
		}
	}
	return root
}

// 不使用额外空间
func connect2(root *Node) *Node {
	if root == nil {
		return nil
	}
	pre := root
	for pre.Left != nil {
		tmp := pre
		for tmp != nil {
			tmp.Left.Next = tmp.Right
			if tmp.Next != nil {
				tmp.Right.Next = tmp.Next.Left
			}
			tmp = tmp.Next
		}
		pre = pre.Left
	}
	return root
}

func main() {
	root := connect(&Node{
		1,
		&Node{2, &Node{4, nil, nil, nil}, &Node{5, nil, nil, nil}, nil},
		&Node{3, &Node{6, nil, nil, nil}, &Node{7, nil, nil, nil}, nil},
		nil,
	})
	fmt.Println(root.Val, root.Left, root.Right, root.Next)
}
