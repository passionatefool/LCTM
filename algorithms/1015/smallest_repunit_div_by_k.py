class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        s = set()
        mod = 0
        i = 1
        while True:
            mod = (mod * 10 + 1) % k
            if mod in s:
                return -1
            if mod == 0:
                return i
            i += 1
            s.add(mod)


if __name__ == "__main__":
    print(Solution().smallestRepunitDivByK(1))
    print(Solution().smallestRepunitDivByK(3))
