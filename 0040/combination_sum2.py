from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.handle(candidates, target, res, [], 0, 0)
        return res

    def handle(self, candidates: List[int], target: int, res: List[List[int]], cur: List[int], cur_sum: int,
               index: int):
        if cur_sum == target:
            res.append(cur.copy())
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i - 1] == candidates[i]:
                continue
            num = candidates[i]
            if cur_sum + num <= target:
                cur.append(num)
                cur_sum += num
                self.handle(candidates, target, res, cur, cur_sum, i + 1)
                cur_sum -= num
                cur.pop()


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
