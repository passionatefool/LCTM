from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.handle(s, res, [], 0)
        return res

    def handle(self, s: str, res: List[List[str]], cur: List[str], index: int):
        if index >= len(s) and len(cur) > 0:
            res.append(cur.copy())
            return
        for i in range(index, len(s)):
            ss = s[index:i + 1]
            if not self.is_partition(ss):
                continue
            cur.append(ss)
            self.handle(s, res, cur, i + 1)
            cur.pop()

    def is_partition(self, s: str) -> bool:
        for i in range(0, len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True


if __name__ == "__main__":
    print(Solution().partition("aab"))
