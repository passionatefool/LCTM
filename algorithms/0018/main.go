package main

import (
	"fmt"
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	res := make([][]int, 0)
	length := len(nums)
	if length < 4 {
		return res
	}
	sort.Ints(nums)

	for i := 0; i < length-3; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		if nums[i]+nums[length-1]+nums[length-2]+nums[length-3] < target {
			continue
		}

		if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target {
			return res
		}

		for j := i + 1; j < length-2; j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			if nums[i]+nums[j]+nums[length-1]+nums[length-2] < target {
				continue
			}

			if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target {
				break
			}

			lp := j + 1
			rp := length - 1
			for lp < rp {
				if nums[i]+nums[j]+nums[lp]+nums[rp] == target {
					res = append(res, []int{nums[i], nums[j], nums[lp], nums[rp]})
					for lp < rp && nums[lp] == nums[lp+1] {
						lp++
					}
					for lp < rp && nums[rp] == nums[rp-1] {
						rp--
					}
					lp++
					rp--
				} else if nums[i]+nums[j]+nums[rp]+nums[lp] < target {
					lp++
				} else {
					rp--
				}
			}
		}
	}
	return res
}

func main() {
	fmt.Println(fourSum([]int{1, 0, -1, 0, -2, 2}, 0))
	fmt.Println(fourSum([]int{-2, -1, -1, 1, 1, 2, 2}, 0))
}
