package main;

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[][] m = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            m[i][0] = i;
            m[i][1] = nums[i];
        }
        Arrays.sort(m, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        int[] result = new int[nums.length];
        int p = -1;
        for (int i = 0; i < m.length; i++) {
            if (p == -1 || m[i - 1][1] != m[i][1]) {
                p = i;
            }
            result[m[i][0]] = p;
        }
        return result;
    }
}
