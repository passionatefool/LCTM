from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        self.backtrack(s, wordDict, res, [], 0)
        return res

    def backtrack(self, s: str, wordDict: List[str], res: List[str], cur: List[str], index: int):
        if index >= len(s):
            res.append(' '.join(cur))
            return
        for word in wordDict:
            if index + len(word) <= len(s) and s[index:index + len(word)] == word:
                cur.append(word)
                self.backtrack(s, wordDict, res, cur, index + len(word))
                cur.pop()


if __name__ == "__main__":
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
