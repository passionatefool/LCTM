package main

import "fmt"

func isUgly(n int) bool {
	if n == 0 {
		return false
	}
	for n != 1 {
		if n%2 == 0 {
			n = n/2
		} else if n%3 == 0 {
			n = n/3
		} else if n%5 == 0 {
			n = n/5
		} else {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isUgly(14))
	fmt.Println(isUgly(8))
}
