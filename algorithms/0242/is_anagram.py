class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for item in s:
            h[item] = h.get(item, 0) + 1
        for item in t:
            if h.get(item, 0) == 0:
                return False
            else:
                h[item] -= 1
        for k in h:
            if h[k] > 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
