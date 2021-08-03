class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1n, s2n = len(s1), len(s2)
        if s1n > s2n:
            return False
        h = {}
        for i in range(s1n):
            h[s1[i]] = h.get(s1[i], 0) - 1
            h[s2[i]] = h.get(s2[i], 0) + 1
        diff = 0
        for k in h:
            diff += (1 if h[k] != 0 else 0)
        if diff == 0:
            return True
        for i in range(s1n, s2n):
            x, y = s2[i], s2[i - s1n]
            if x == y:
                continue
            if h.get(x, 0) == 0:
                diff += 1
            h[x] = h.get(x, 0) + 1
            if h[x] == 0:
                diff -= 1

            if h.get(y, 0) == 0:
                diff += 1
            h[y] = h.get(y, 0) - 1
            if h[y] == 0:
                diff -= 1
            if diff == 0:
                return True
        return False


if __name__ == "__main__":
    print(Solution().checkInclusion("ab", "eidbaooo"))
    print(Solution().checkInclusion("ab", "eidboaoo"))
