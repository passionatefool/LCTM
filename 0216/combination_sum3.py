from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.handle(n, k, 1, [], res)
        return res

    def handle(self, n: int, k: int, index: int, cur: List[int], res: List[List[int]]):
        cur_sum = sum(cur)
        if len(cur) == k and cur_sum == n:
            res.append(cur.copy())
            return
        for i in range(index, 10):
            if cur_sum > n:
                return
            cur.append(i)
            self.handle(n, k, i + 1, cur, res)
            cur.pop()


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))
