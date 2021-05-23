package main

import "fmt"

func isValid(s string) bool {
	stack := []uint8{}
	for i := 0; i < len(s); i++ {
		v := s[i]
		if v == '(' || v == '{' || v == '[' {
			stack = append(stack, v)
		} else {
			if len(stack) == 0 {
				return false
			}
			top := stack[len(stack) - 1]
			if (top == '(' && v == ')') || (top == '[' && v == ']') || (top == '{' && v == '}') {
				stack = stack[:len(stack) - 1]
			} else {
				return false
			}
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("{[]}"))

}
