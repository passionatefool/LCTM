from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.handle(s, res, [], 0)
        return res

    def handle(self, s: str, res: List[str], cur: List[str], index: int):
        if len(cur) > 4:
            return
        if index >= len(s) and len(cur) == 4:
            res.append('.'.join(cur))
            return
        for i in range(index, len(s)):
            ss = s[index:i + 1]
            if not self.is_valid(ss):
                continue
            cur.append(ss)
            self.handle(s, res, cur, i + 1)
            cur.pop()

    def is_valid(self, s: str) -> bool:
        if len(s) > 1 and int(s[0]) == 0:
            return False
        i = int(s)
        return 0 <= i <= 255


if __name__ == "__main__":
    print(Solution().restoreIpAddresses("25525511135"))
