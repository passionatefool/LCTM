from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result, index = 0, 0
        for si in s:
            if index < len(g) and si >= g[index]:
                result += 1
                index += 1
        return result


if __name__ == "__main__":
    print(Solution().findContentChildren([1, 2, 3], [1, 1]))
