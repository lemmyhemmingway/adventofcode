use std::fs;

fn main() {
    part1();
    part2();
}

fn part1() {
    let contents = fs::read_to_string("../../inputs/day1.txt").expect("No file");
    let contents = contents.chars();
    let mut floor = 0;
    for item in contents {
        if item == '(' {
            floor += 1;
        } else if item == ')' {
            floor -= 1;
        }
    }
    println!("{floor}");
}

fn part2() {
    let contents = fs::read_to_string("../../inputs/day1.txt").expect("No file");
    let contents = contents.chars();
    let mut floor = 0;
    let mut position = 0;
    for item in contents {
        position += 1;
        if item == '(' {
            floor += 1;
        } else if item == ')' {
            floor -= 1;
        }
        if floor == -1 {
            println!("{position}");
            break;
        }
    }

}
