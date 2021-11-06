package main

import "fmt"

func largestRectangleArea(heights []int) int {
	res := 0
	stack := make([]int, 0, len(heights))
	heights = append([]int{0}, heights...)
	heights = append(heights, 0)
	stack = append(stack, 0)
	for i := 1; i < len(heights); i++ {
		for ; heights[i] < heights[stack[len(stack)-1]]; {
			m := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			h := heights[m]
			w := i - stack[len(stack)-1] - 1
			res = max(res, h*w)
		}
		stack = append(stack, i)
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}))
	//fmt.Println(largestRectangleArea([]int{2, 4}))
}
