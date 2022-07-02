// 3474. 교수가 된 현우

use std::io;

fn main() {
    let mut input = String::new();
    let stdin = io::stdin();

    stdin.read_line(&mut input).unwrap();
    let t: usize = input.trim().parse().unwrap();

    let mut lst = vec![];
    for _ in 0..t {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let n: u32 = input.trim().parse().unwrap();

        let (mut ans, mut div) = (0, 5);
        while div <= n {
            ans += n / div;
            div *= 5;
        }
        lst.push(ans.to_string())
    }

    println!("{}", lst.join("\n"))
}
