package main

import (
	"fmt"
	"sort"
)

// 1. 排序
// 2. 遍历排序后的数组：i
//    - 当 nums[i] > 0，则后面和已无法为 0，遍历结束，返回
//    - 碰到相同元素则跳过 nums[i] == nums[i-1]
//	  - 令左指针 lp = i + 1, 右指针 rp = len(nums) - 1，循环往中间靠拢
//        - 和为 0，添加进结果，并继续去重，lp rp 都移到下一个位置
// 		  - 和大于 0，rp 左移，和小于 0，lp 右移
func threeSum(nums []int) [][]int {
	res := make([][]int, 0)
	if len(nums) < 3 {
		return res
	}
	sort.Ints(nums)

	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			return res
		}
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		lp := i + 1
		rp := len(nums) - 1

		for lp < rp {
			if nums[i]+nums[lp]+nums[rp] == 0 {
				res = append(res, []int{nums[i], nums[lp], nums[rp]})
				for lp < rp && nums[lp] == nums[lp+1] {
					lp++
				}
				for lp < rp && nums[rp] == nums[rp-1] {
					rp--
				}
				lp++
				rp--
			} else if nums[i]+nums[lp]+nums[rp] > 0 {
				rp--
			} else {
				lp++
			}
		}
	}
	return res
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
	fmt.Println(threeSum([]int{0, 0, 0, 0, 0, 0}))
}
