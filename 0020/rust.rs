
struct Solution {

}

impl Solution {
    fn is_left(c: char) -> bool {
        if c == '(' || c == '{' || c == '[' {
            return true;
        }
        return false;
    }
    fn is_right(c: char) -> bool {
        if c == ')' || c == '}' || c == ']' {
            return true
        }
        return false
    }
    fn is_match(left: char, right: char) -> bool {
        if left == '(' {
            return right == ')';
        }
        if left == '[' {
            return right == ']';
        }
        if left == '{' {
            return right == '}';
        }
        return false
    }
    pub fn is_valid(s: String) -> bool {
        let mut v: Vec<char> = Vec::new();
        if s.len() % 2 != 0 {
            return false
        }
        for (i, c) in s.chars().enumerate() {
            if Solution::is_left(c) {
                v.push(c);
            } else {
                let len = v.len();
                if len == 0 {
                    return false
                }
                let left = v[len - 1];
                if !Solution::is_match(left, c) {
                    return false
                }
                v.pop();
                if v.len() == 0 && i == s.len() - 1{
                    return true
                }
            }
        }
        return false;
    }
}

fn main() {
    println!("{}", Solution::is_valid("[[]]]".to_string()));
}