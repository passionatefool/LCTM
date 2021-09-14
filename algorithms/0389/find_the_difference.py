class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for c in s + t:
            res ^= ord(c)
        return chr(res)


if __name__ == "__main__":
    print(Solution().findTheDifference("abcd", "abcde"))
    print(Solution().findTheDifference("ae", "aea"))
