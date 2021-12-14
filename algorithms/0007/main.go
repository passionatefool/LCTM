package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	var isNegative bool
	var res int
	if x < 0 {
		isNegative = true
		x = -x
	} else {
		isNegative = false
	}
	for x != 0 {
		if res < math.MinInt32/10 || res > math.MaxInt32/10 {
			return 0
		}
		y := x % 10
		x /= 10
		res = res*10 + y
	}
	if isNegative {
		res = -res
	}

	return res
}

func main() {
	fmt.Println(reverse(-123))
}
