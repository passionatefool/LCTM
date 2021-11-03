package main

import "fmt"

func trap(height []int) int {
	res := 0
	stack := make([]int, 0, len(height))
	stack = append(stack, 0)
	for i := 1; i < len(height); i++ {
		for ; len(stack) > 0 && height[i] > height[stack[len(stack)-1]]; {
			m := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if len(stack) > 0 {
				h := min(height[i], height[stack[len(stack)-1]]) - height[m]
				w := i - stack[len(stack)-1] - 1
				res += h * w
			}
		}
		stack = append(stack, i)
	}
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	//fmt.Println(trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
	fmt.Println(trap([]int{4, 2, 0, 3, 2, 5}))
}
