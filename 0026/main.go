package main

import "fmt"

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	count := 1
	preNum := nums[0]
	for _, v := range nums {
		if v != preNum {
			preNum = v
			nums[count] = v
			count += 1
		}
	}
	return count
}

func main() {
	fmt.Println(removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}))

}
