from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(r, c: int) -> int:
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0

            grid[r][c] = 2
            return dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return 0


if __name__ == "__main__":
    print(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
