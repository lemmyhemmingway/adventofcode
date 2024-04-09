use std::{char, fs};

const FILEPATH: &str = "../../inputs/day1.txt";

fn read_file(filepath: &str) -> Vec<char> {
    let contents = fs::read_to_string(&filepath).expect("couldn't read the file");
    contents.chars().collect()
}

fn part1(contents: Vec<char>) -> i32 {
    let mut result = 0;
    for content in contents {
        match content {
            '(' => result += 1,
            ')' => result -= 1,
            _ => result += 0,
        }
    }
    result
}

fn part2(contents: Vec<char>) -> i32 {
    let mut result = 0;
    for (index, content) in contents.into_iter().enumerate() {
        match content {
            '(' => result += 1,
            ')' => result -= 1,
            _ => result += 0,
        }
        if result == -1 {
            return index as i32 + 1;
        }
    }
    result
}

fn main() {
    let contents = read_file(FILEPATH);
    let part1_result = part1(contents.clone());
    let part2_result = part2(contents);
    println!("{}", part1_result);
    println!("{}", part2_result);

}

#[test]
fn test_empty_vector() {
    let result = part1(vec!['(', '(', ')', ')']);
    assert_eq!(0, result);
}

#[test]
fn test_floor_zero() {
    let result = part1(vec!['(', '(', ')', ')']);
    assert_eq!(0, result);
}
#[test]
fn test_floor_three() {
    let result = part1(vec![')', ')', '(', '(', '(', '(', '(']);
    assert_eq!(3, result);
}

#[test]
fn test_floor_minus_three() {
    let result = part1(vec![')', '(', ')', ')', '(', ')', ')']);
    assert_eq!(-3, result);
}
