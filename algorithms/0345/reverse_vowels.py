class Solution:
    def reverseVowels(self, s: str) -> str:
        ss=list(s)
        l = 0
        r = len(ss) - 1
        m = ['a', 'e', 'i', 'o', 'u']
        while l < r:
            while l < r and ss[l].lower() not in m:
                l += 1
            while l < r and ss[r].lower() not in m:
                r -= 1
            if l < r:
                ss[l], ss[r] = ss[r], ss[l]
                l, r = l + 1, r - 1
        return ''.join(ss)


if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))
