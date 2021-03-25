package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	res := make([]int, 0, m+n)
	i, j := 0, 0
	for i < m || j < n {
		if i == m {
			res = append(res, nums2[j])
			j++
		} else if j == n {
			res = append(res, nums1[i])
			i++
		} else if nums1[i] < nums2[j] {
			res = append(res, nums1[i])
			i++
		} else {
			res = append(res, nums2[j])
			j++
		}
	}
	copy(nums1, res)
}

func main() {
	num1 := []int{1, 2, 3, 0, 0, 0}
	num2 := []int{2, 5, 6}
	merge(num1, 3, num2, 3)
	fmt.Println(num1)

}
