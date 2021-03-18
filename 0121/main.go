package main

import (
	"fmt"
)

func maxProfit(prices []int) int {
	minPrice, profit := prices[0], 0
	for i := 1; i < len(prices); i++ {
		tmp := prices[i] - minPrice
		if tmp > profit {
			profit = tmp
		}
		if prices[i] < minPrice {
			minPrice = prices[i]
		}
	}
	return profit
}

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}
