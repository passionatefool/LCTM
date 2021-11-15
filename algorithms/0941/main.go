package main

import "fmt"

func validMountainArray(arr []int) bool {
	if len(arr) < 3 {
		return false
	}
	breakPoint := 0
	hasLeft := false
	for i := 1; i < len(arr); i++ {
		if arr[i] <= arr[i-1] {
			breakPoint = i
			break
		} else {
			hasLeft = true
		}
	}
	if hasLeft == false {
		return false
	}
	if breakPoint == 0 {
		return false
	}
	for i := breakPoint; i < len(arr); i++ {
		if arr[i] >= arr[i-1] {
			return false
		}
	}
	return true
}

func main() {
	//fmt.Println(validMountainArray([]int{0, 2, 3, 4, 5, 2, 1, 0}))
	//fmt.Println(validMountainArray([]int{0, 2, 3, 3, 5, 2, 1, 0}))
	fmt.Println(validMountainArray([]int{0, 1, 2, 3, 4, 5, 6, 7}))
	//fmt.Println(validMountainArray([]int{1, 3, 2}))
	//fmt.Println(validMountainArray([]int{7, 6, 5, 4, 3, 2, 1, 0}))
}
