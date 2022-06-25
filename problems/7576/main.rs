// 7576. 토마토

use std::io;

fn connected_positions((n, m): (usize, usize), (col, row): (usize, usize)) -> Vec<(usize, usize)> {
    let mut positions = Vec::new();

    if col > 0 {
        positions.push((col - 1, row));
    }
    if col < n - 1 {
        positions.push((col + 1, row));
    }
    if row > 0 {
        positions.push((col, row - 1));
    }
    if row < m - 1 {
        positions.push((col, row + 1));
    }

    positions
}

fn propagate(tomatoes: &mut Vec<Vec<i32>>, pos: (usize, usize)) -> Vec<(usize, usize)> {
    let (n, m) = (tomatoes.len(), tomatoes[0].len());
    let mut propagated = Vec::new();

    let connected = connected_positions((n, m), pos);
    for con in connected {
        if tomatoes[con.0][con.1] != 0 {
            continue;
        }

        tomatoes[con.0][con.1] = 1;
        propagated.push(con);
    }

    propagated
}

fn ripen(tomatoes: &mut Vec<Vec<i32>>, target: usize) -> i32 {
    let (n, m) = (tomatoes.len(), tomatoes[0].len());
    let mut ripening = Vec::new();
    for col in 0..n {
        for row in 0..m {
            if tomatoes[col][row] == 1 {
                ripening.push((col, row));
            }
        }
    }

    let mut current = ripening.len();
    let mut days = 0;
    while current != target {
        let mut to_be_ripening = Vec::new();
        for (col, row) in ripening {
            to_be_ripening.append(&mut propagate(tomatoes, (col, row)));
        }

        if to_be_ripening.len() == 0 {
            return -1;
        }
        ripening = to_be_ripening;
        current += ripening.len();
        days += 1;
    }

    days
}

fn solve(tomatoes: &mut Vec<Vec<i32>>) -> i32 {
    let (n, m) = (tomatoes.len(), tomatoes[0].len());
    let mut hollow = 0;
    for col in 0..n {
        for row in 0..m {
            if tomatoes[col][row] == -1 {
                hollow += 1;
            }
        }
    }

    ripen(tomatoes, m * n - hollow)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let input: Vec<usize> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let (m, n) = (input[0], input[1]);
    let mut tomatoes = vec![vec![-1; m]; n];
    for col in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        let line: Vec<i32> = input
            .trim()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        for (row, &tomato) in line.iter().enumerate() {
            tomatoes[col][row] = tomato;
        }
    }

    println!("{}", solve(&mut tomatoes));
}
