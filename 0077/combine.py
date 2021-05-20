from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.handle(n, k, 1, [], res)
        return res

    def handle(self, n: int, k: int, index: int, cur: List[int], res: List[List[int]]):
        if len(cur) == k:
            res.append(cur.copy())
            return
        for i in range(index, n+2-(k-len(cur))):
            cur.append(i)
            self.handle(n, k, i + 1, cur, res)
            cur.pop()


if __name__ == "__main__":
    print(Solution().combine(4, 2))
