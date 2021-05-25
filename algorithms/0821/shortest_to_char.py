from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        result = []
        for i in range(len(S)):
            l = r = 0
            while i - l >= 0:
                if S[i - l] == C:
                    break
                l += 1
            while i + r < len(S):
                if S[i + r] == C:
                    break
                r += 1
            if i - l == -1:
                l = 10000
            if i + r == len(S):
                r = 10000
            result.append(min(l, r))
        return result


if __name__ == "__main__":
    print(Solution().shortestToChar("loveleetcode", "e"))
