package main;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0, max = 0;
        Map<Character, Integer> m = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            if (m.containsKey(s.charAt(i))) {
                Integer val = m.get(s.charAt(i));
                if (start < val) {
                    start = val + 1;
                }
            }
            if (i - start + 1 > max) {
                max = i - start + 1;
            }
            m.put(s.charAt(i), i);
        }
        return max;
    }
}
