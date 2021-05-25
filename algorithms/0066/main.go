package main

import "fmt"

func plusOne(digits []int) []int {
	for i := len(digits) -1; i >= 0; i-- {
		digits[i] ++
		if digits[i] != 10 {
			return digits
		} else {
			digits[i] = 0
		}
	}
	digits[0] = 1
	return append(digits, 0)
}

func main()  {
	fmt.Println(plusOne([]int{9}))
}
