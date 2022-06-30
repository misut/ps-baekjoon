// 1149. RGB거리

use std::cmp;
use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let n = input.trim().parse().unwrap();

    let mut temp = [0u32; 3];
    let mut prices = [0u32; 3];
    for _ in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        for (idx, price) in input.split_whitespace().enumerate() {
            temp[idx] = price.trim().parse().unwrap();
        }

        temp[0] += cmp::min(prices[1], prices[2]);
        temp[1] += cmp::min(prices[0], prices[2]);
        temp[2] += cmp::min(prices[0], prices[1]);
        prices = temp;
    }

    println!("{}", prices.iter().min().unwrap());
}
