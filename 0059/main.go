package main

import "fmt"

func generateMatrix(n int) [][]int {
	mtr := make([][]int, n)
	for i := range mtr {
		mtr[i] = make([]int, n)
	}
	sum := 1
	left, right, top, bottom := 0, n-1, 0, n-1
	for sum <= n*n {
		for i := left; i <= right; i++ {
			mtr[top][i] = sum
			sum++
		}
		top++
		for i := top; i <= bottom; i++ {
			mtr[i][right] = sum
			sum++
		}
		right--
		for i := right; i >= left; i-- {
			mtr[bottom][i] = sum
			sum++
		}
		bottom--
		for i := bottom; i >= top; i-- {
			mtr[i][left] = sum
			sum++
		}
		left++
	}
	return mtr
}

func main() {
	fmt.Println(generateMatrix(3))
}
