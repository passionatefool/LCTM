package main;

class Solution {
    public int tribonacci(int n) {
        if (n <= 1) return n;
        if (n == 2) return 1;
        int total = 0, a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            total = a + b + c;
            a = b;
            b = c;
            c = total;
        }
        return total;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.tribonacci(0));
        System.out.println(solution.tribonacci(1));
        System.out.println(solution.tribonacci(2));
    }
}
