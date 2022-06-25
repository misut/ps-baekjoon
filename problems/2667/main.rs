// 2667. 단지번호붙이기

use std::io;

fn generate_candidates(
    pos: (usize, usize),
    size: usize,
    visited: &mut [[bool; 25]; 25],
) -> Vec<(usize, usize)> {
    let mut candidates: Vec<(usize, usize)> = vec![];

    if pos.0 > 0 && !visited[pos.0 - 1][pos.1] {
        candidates.push((pos.0 - 1, pos.1));
    }
    if pos.0 < size - 1 && !visited[pos.0 + 1][pos.1] {
        candidates.push((pos.0 + 1, pos.1));
    }
    if pos.1 > 0 && !visited[pos.0][pos.1 - 1] {
        candidates.push((pos.0, pos.1 - 1));
    }
    if pos.1 < size - 1 && !visited[pos.0][pos.1 + 1] {
        candidates.push((pos.0, pos.1 + 1));
    }

    candidates
}

fn find_village(
    pos: (usize, usize),
    board: &[[i32; 25]; 25],
    size: usize,
    visited: &mut [[bool; 25]; 25],
) -> usize {
    let mut candidates = vec![pos];
    let mut village = 0;

    while candidates.len() > 0 {
        let pos = candidates.remove(0);
        if !(0..size).contains(&pos.0) || !(0..size).contains(&pos.1) || visited[pos.0][pos.1] {
            continue;
        }

        visited[pos.0][pos.1] = true;
        if board[pos.0][pos.1] == 0 {
            continue;
        }

        village += 1;
        candidates.append(&mut generate_candidates(pos, size, visited));
    }

    village
}

fn solve(board: &[[i32; 25]; 25], size: usize) -> Vec<usize> {
    let mut visited = [[false; 25]; 25];

    let mut result: Vec<usize> = vec![];
    for col in 0..size {
        for row in 0..size {
            let pos = (col, row);
            if visited[pos.0][pos.1] {
                continue;
            }

            let village = find_village(pos, board, size, &mut visited);
            if village > 0 {
                result.push(village);
            }
        }
    }

    result.sort();
    result
}

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read line");

    let n: usize = n.trim().parse().expect("Cannot parse N");
    let mut board = [[0; 25]; 25];
    for col in 0..n {
        let mut line = String::new();
        io::stdin()
            .read_line(&mut line)
            .expect("Failed to read line");

        for (row, house) in line.trim().chars().enumerate() {
            board[col][row] = house as i32 - '0' as i32;
        }
    }

    let result = solve(&board, n);
    println!("{}", result.len());
    for village in result.iter() {
        println!("{}", village);
    }
}
