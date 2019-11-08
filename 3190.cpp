#include <iostream>

using namespace std;

int N, K, L;
int dc[4] = {-1, 0, 1, 0};
int dr[4] = {0, -1, 0, 1};
int brd[100][100] = {0, };
int lev[100][2] = {0, };

int main() {
    cin >> N >> K;
    for( int i = 0; i < K; ++i ) {
        int pc, pr;
        cin >> pc >> pr;
        brd[pc-1][pr-1] = 2;
    }
    cin >> L;
    for( int i = 0; i < L; ++i ) {
        char ch;
        cin >> lev[i][0] >> ch;
        if( ch == 'L' ) lev[i][1] = 1;
        else            lev[i][1] = -1;
    }
    int pc = 0, pr = 0, lc = 0, lr = 0, dir = 3, t = 0, cl = 0, ap = 0, ldir = 3, lcl = 0;
    brd[pc][pr] = 1;
    while( 1 ) {
        pc += dc[dir];
        pr += dr[dir];
        if( pc<0 || pc>=N || pr<0 || pr>=N || brd[pc][pr] == 1 ) break;
        if( brd[pc][pr] == 2 ) {
            ap++;
        }
        else {
            brd[lc][lr] = 0;
            lc += dc[ldir];
            lr += dr[ldir];
        }
        brd[pc][pr] = 1;
        t++;
        if( t == lev[cl][0] ) {
            dir = (dir+lev[cl][1])%4;
            if( dir < 0 ) dir += 4;
            cl++;
        }
        if( t-ap == lev[lcl][0] ) {
            ldir = (ldir+lev[lcl][1]) % 4;
            if( ldir < 0 ) ldir += 4;
            lcl++;
        }
    }
    cout << t+1 << endl;
}
