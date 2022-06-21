// 7568. 덩치

use std::io;

fn solve(bulks: &[(i32, i32); 50], ranks: &mut [i32; 50]) {
    for rank in ranks.iter_mut() {
        *rank = 1;
    }
    for (idx, bulk) in bulks.iter().enumerate() {
        for other in bulks.iter() {
            if bulk.0 < other.0 && bulk.1 < other.1 {
                ranks[idx] += 1;
            }
        }
    }
}

fn main() {
    let mut trial = String::new();
    io::stdin().read_line(&mut trial).expect("Failed to read N");

    let trial = trial.trim().parse().expect("Cannot parse N");
    let mut bulks = [(0, 0); 50];
    for idx in 0..trial {
        let mut bulk = String::new();
        io::stdin()
            .read_line(&mut bulk)
            .expect("Failed to read bulk");

        let bulk: Vec<&str> = bulk.trim().split_whitespace().collect();
        let bulk: (i32, i32) = (
            bulk[0].parse().expect("Cannot parse weight"),
            bulk[1].parse().expect("Cannot parse height"),
        );
        bulks[idx] = bulk;
    }

    let mut ranks = [1; 50];
    solve(&bulks, &mut ranks);

    for idx in 0..trial {
        print!("{rank} ", rank = ranks[idx]);
    }
}
