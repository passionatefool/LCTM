package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	numStack := []int{}
	for _, v := range tokens {
		if v == "+" || v == "-" || v == "*" || v == "/" {
			n2 := numStack[len(numStack)-1]
			n1 := numStack[len(numStack)-2]
			numStack = numStack[:len(numStack)-2]
			switch v {
			case "+":
				numStack = append(numStack, n1+n2)
			case "-":
				numStack = append(numStack, n1-n2)
			case "*":
				numStack = append(numStack, n1*n2)
			case "/":
				numStack = append(numStack, n1/n2)
			}
		} else {
			vv, _ := strconv.Atoi(v)
			numStack = append(numStack, vv)
		}
	}
	return numStack[0]
}

func main() {
	fmt.Println(evalRPN([]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}))
}
