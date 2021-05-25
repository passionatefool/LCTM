package main

import (
	"fmt"
	"strings"
)

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	left, right := 0, len(s) -1
	for left < right {
		for left < right && !isAlNum(s[left]) {
			left ++
		}
		for left < right && !isAlNum(s[right]) {
			right --
		}
		if s[left] != s[right] {
			return false
		} else {
			left ++
			right --
		}
	}
	return true
}

func isAlNum(c byte) bool {
	return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')
}

func main() {
	fmt.Println(isAlNum(','))
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("race a car"))
}
