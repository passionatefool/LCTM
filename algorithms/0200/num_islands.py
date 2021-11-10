from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c: int):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if grid[r][c] != '1':
                return
            grid[r][c] = 2
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count


if __name__ == "__main__":
    s = Solution()
    print(Solution().numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
