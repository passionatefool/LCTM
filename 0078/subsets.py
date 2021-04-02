from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            tmp = []
            for r in result:
                nr = r.copy()
                nr.append(num)
                tmp.append(nr)
            result.extend(tmp)
        return result


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
