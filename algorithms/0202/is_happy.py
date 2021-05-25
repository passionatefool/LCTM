class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            sum = 0
            while n != 0:
                v = n % 10
                sum += v * v
                n = int(n/10)
            if sum == 1:
                return True
            if sum in s:
                return False
            s.add(sum)
            n = sum


if __name__ == "__main__":
    print(Solution().isHappy(19))
