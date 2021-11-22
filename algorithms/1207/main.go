package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	count := make([]int, 2001)
	flag := make([]bool, 1001)
	for i := 0; i < len(arr); i++ {
		count[arr[i]+1000]++
	}
	for i := 0; i < len(count); i++ {
		if count[i] > 0 {
			if flag[count[i]] == false {
				flag[count[i]] = true
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Println(uniqueOccurrences([]int{1, 2, 2, 1, 1, 3}))
	fmt.Println(uniqueOccurrences([]int{1, 2}))
	fmt.Println(uniqueOccurrences([]int{-3, 0, 1, -3, 1, 1, 1, -3, 10, 0}))
}
