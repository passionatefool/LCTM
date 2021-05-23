use std::collections::HashMap;
use std::cmp;
struct Solution {

}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut m = HashMap::new();
        let mut ret: i32 = 0;
        let mut start: i32 = 0;
        for (i, c) in s.chars().enumerate() {
            if m.contains_key(&c) {
                start = cmp::max(start, (m[&c] + 1) as i32);  
            }
            ret = cmp::max(ret, i as i32 - start + 1);
            m.insert(c, i);
        }
        return ret 
    }
}

fn main() {
    println!("{}", Solution::length_of_longest_substring("123".to_string()));
}