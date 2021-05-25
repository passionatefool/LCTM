class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = {}
        for s in magazine:
            if s in h:
                h[s] += 1
            else:
                h[s] = 1
        for s in ransomNote:
            if s not in h:
                return False
            h[s] -= 1
            if h[s] == 0:
                del h[s]
        return True


if __name__ == "__main__":
    print(Solution().canConstruct("aa", "aab"))
