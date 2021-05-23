from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) != 0:
            h = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
            self.handle(digits, 0, [], res, h)
        return res

    def handle(self, digits: str, index: int, cur: List[str], res: List[str], h: List[str]):
        if len(cur) == len(digits):
            res.append(''.join(cur))
            return

        hs = h[int(digits[index])]
        for s in hs:
            cur.append(s)
            self.handle(digits, index + 1, cur, res, h)
            cur.pop()


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
