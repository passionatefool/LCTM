package main

import "fmt"

func maxProfit(prices []int, fee int) int {
	res := 0
	minPrice := prices[0]
	for i := 1; i < len(prices); i++ {
		// buy
		if prices[i] < minPrice {
			minPrice = prices[i]
		}

		if prices[i] >= minPrice && prices[i] <= minPrice+fee {
			continue
		}
		// sell
		if prices[i] > minPrice+fee {
			res += prices[i] - minPrice - fee
			minPrice = prices[i] - fee
		}
	}
	return res
}

func main() {
	fmt.Println(maxProfit([]int{1, 3, 2, 8, 4, 9}, 2))
}
