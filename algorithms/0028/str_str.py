class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle)+1):
            end = i + len(needle)
            if haystack[i:end] == needle:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "bba"))
    print(s.strStr("", ""))
    print(s.strStr("abc", "c"))
