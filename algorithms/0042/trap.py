from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack, result = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                t = stack.pop()
                if stack:
                    result += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] - 1)
            stack.append(i)
        return result


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
