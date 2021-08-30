package main

import (
	"fmt"
	"strconv"
)

func monotoneIncreasingDigits(n int) int {
	s := []uint8(strconv.Itoa(n))

	for i := len(s)-1; i > 0; i-- {
		if s[i-1] > s[i] {
			s[i-1] -= 1
			for j := i; j < len(s); j++ {
				s[j] = '9'
			}
		}
	}
	res, _ := strconv.Atoi(string(s))
	return res
}

func main() {
	fmt.Println(monotoneIncreasingDigits(329))
	fmt.Println(monotoneIncreasingDigits(100))
}
