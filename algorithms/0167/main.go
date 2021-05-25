package main

func twoSum(numbers []int, target int) []int {
	start, end := 0, len(numbers) - 1
	for start != end {
		if numbers[start] + numbers[end] > target {
			end --
		} else if numbers[start] + numbers[end] < target {
			start ++
		} else {
			return []int{start + 1, end + 1}
		}
	}
	return []int{}
}

func main() {

}
