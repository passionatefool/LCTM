class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        h = {}
        max_len = left = right = 0
        while right < len(s):
            si = s[right]
            right += 1
            h[si] = h.get(si, 0) + 1
            while h.get(si, 0) > 1:
                sl = s[left]
                h[sl] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
