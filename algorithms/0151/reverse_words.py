class Solution:
    def reverseWords(self, s: str) -> str:
        ss = list(s)
        self.reverse_str(ss, 0, len(s) - 1)
        left, right = 0, 0
        while right < len(ss):
            while right < len(ss) and not ss[right].isspace():
                right += 1
            self.reverse_str(ss, left, right - 1)
            right += 1
            left = right

        left, right = 0, len(ss) - 1
        while left < right and ss[left].isspace():
            left += 1
        while left < right and ss[right].isspace():
            right -= 1
        ss = ss[left:right + 1]

        res = [ss[0]]
        for i in range(1, len(ss)):
            if res[-1].isspace() and ss[i].isspace():
                continue
            res.append(ss[i])
        return ''.join(res)

    def reverse_str(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1


if __name__ == "__main__":
    print(Solution().reverseWords("  the sky is blue   "))
