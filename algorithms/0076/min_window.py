class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur, expected = {}, {}
        for ss in t:
            expected[ss] = expected.get(ss, 0) + 1
        left, right = 0, 0
        start, end = 0, 0
        match = 0
        min_result = None
        while right < len(s):
            c = s[right]
            right += 1
            if expected.get(c,0) != 0:
                cur[c] = cur.get(c, 0) + 1
                if cur[c] == expected[c]:
                    match += 1
            while match == len(expected):
                if min_result is None or right - left < min_result:
                    min_result = right - left
                    start, end = left, right
                c = s[left]
                left += 1
                if expected.get(c, 0) != 0:
                    if cur[c] == expected[c]:
                        match -= 1
                    cur[c] -= 1
        if min_result is None:
            return ""
        return s[start:end]


if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
