package main

import (
	"fmt"
)

func removeDuplicates(s string) string {
	stack := []rune{}
	for _, v := range s {
		stack = append(stack, v)
		if len(stack) > 1 && stack[len(stack)-1] == stack[len(stack)-2] {
			stack = stack[:len(stack)-2]
		}
	}
	return string(stack)
}

func main() {
	fmt.Println(removeDuplicates("abbaca"))
}
