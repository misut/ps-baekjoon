// 2739. 구구단

use std::io;

fn main() {
    let mut number = String::new();

    io::stdin()
        .read_line(&mut number)
        .expect("Failed to read line");

    let number: i32 = number.trim().parse().expect("Cannot parse number");

    for multiplier in 1..10 {
        println!("{} * {} = {}", number, multiplier, number * multiplier);
    }
}
