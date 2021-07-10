package main

func lengthOfLongestSubstring(s string) int {
	start, maxLength := 0, 0
	var m = map[byte]int{}
	for i := 0; i < len(s); i++ {
		val, ok := m[s[i]]
		if ok && start <= val {
			start = val + 1
		}
		m[s[i]] = i

		if i-start+1 > maxLength {
			maxLength = i - start + 1
		}
	}

	return maxLength
}
