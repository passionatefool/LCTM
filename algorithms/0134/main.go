package main

import "fmt"

func canCompleteCircuit(gas []int, cost []int) int {
	rest := 0
	start := 0
	allGas, allCost := 0, 0
	for i := 0; i < len(gas); i++ {
		allGas += gas[i]
		allCost += cost[i]
		rest += gas[i] - cost[i]
		if rest < 0 {
			start = i + 1
			rest = 0
		}
	}
	if allGas < allCost {
		return -1
	}
	return start
}

func main() {
	fmt.Println(canCompleteCircuit([]int{1,2,3,4,5}, []int{3,4,5,1,2}))
}
