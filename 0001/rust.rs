use std::collections::HashMap;

struct Solution {

}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut v: Vec<i32> = Vec::new();
		let mut store = HashMap::new();
		for (idx, num) in nums.iter().enumerate() {
			let gap = target - num;
			if store.contains_key(&gap) {
                v.push(store[&gap] as i32);
                v.push(idx as i32);
			} else {
				store.insert(num, idx);
			}
		}
		return v;
    }
}

fn main() {
	let v = Solution::two_sum(vec![2, 7, 11, 15], 9);
}
