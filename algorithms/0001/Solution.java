package main;

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                int[] result = {map.get(diff), i};
                return result;
            } else {
                map.put(nums[i], i);
            }
        }
        return null;
    }
}
