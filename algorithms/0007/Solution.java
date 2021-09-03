package main;

public class Solution {
    public int reverse(int x) {
        int num = 0;
        while (x != 0) {
            if (num > Integer.MAX_VALUE/10 || num < Integer.MIN_VALUE/10) {
                return 0;
            }
            num = num * 10 + x % 10;
            x = x / 10;
        }
        return num;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        s.reverse(1534236469);
    }
}
