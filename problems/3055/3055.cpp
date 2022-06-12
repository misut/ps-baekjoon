#include <iostream>

using namespace std;

int main () {
    int R, C;
    int dc, dr;
    bool visited[50][50] = {0, };
    char brd[50][50] = {0, };
    int wq[2500][2] = {0, }; // Col, Row
    int chi[2500][3] = {0, }; // Col, Row, Time
    int ws = 0, wl = 0, cs = 0, cl = 0;

    cin >> R >> C;
    for( int c = 0; c < R; ++c ) {
        cin >> brd[c];
        for( int r = 0; r < C; ++r ) {
            switch( brd[c][r] ) {
                case '*':
                    wq[wl][0] = c, wq[wl][1] = r, wl++;
                    break;
                case 'S':
                    chi[cl][0] = c, chi[cl][1] = r, chi[cl][2] = 0, cl++;
                    brd[c][r] = '.';
                    visited[c][r] = true;
                    break;
                case 'D':
                    dc = c, dr = r;
                    break;
                default: break;
            }
        }
    }

    bool esc = false;
    int pt = chi[cs][2];
    while( cl - cs ) {
        int pc = chi[cs][0], pr = chi[cs][1], t = chi[cs][2];
        if( t == pt+1 ) {
            int len = 0;
            int ts = ws, tl = wl;
            pt = t;
            for( int i = ts; i < tl; ++i ) {
                int wc = wq[i][0], wr = wq[i][1];
                if( wc-1 >= 0 && brd[wc-1][wr] == '.' ) {
                    brd[wc-1][wr] = '*';
                    wq[wl][0] = wc-1, wq[wl][1] = wr, wl++; 
                }
                if( wc+1 < R && brd[wc+1][wr] == '.' ) {
                    brd[wc+1][wr] = '*';
                    wq[wl][0] = wc+1, wq[wl][1] = wr, wl++; 
                }
                if( wr-1 >= 0 && brd[wc][wr-1] == '.' ) {
                    brd[wc][wr-1] = '*';
                    wq[wl][0] = wc, wq[wl][1] = wr-1, wl++; 
                }
                if( wr+1 < C && brd[wc][wr+1] == '.' ) {
                    brd[wc][wr+1] = '*';
                    wq[wl][0] = wc, wq[wl][1] = wr+1, wl++; 
                }
                ws++;
            }
        }

        if( brd[pc][pr] == '*' ) {
            cs++;
            continue;
        }
        if( brd[pc][pr] == 'D' ) {
            esc = true;
            break;
        }

        if( pc-1 >= 0 && ( brd[pc-1][pr] == '.' || brd[pc-1][pr] == 'D' ) && !visited[pc-1][pr] ) {
            chi[cl][0] = pc-1, chi[cl][1] = pr, chi[cl][2] = t+1, cl++;
            visited[pc-1][pr] = true;
        }
        if( pc+1 < R && ( brd[pc+1][pr] == '.' || brd[pc+1][pr] == 'D' ) && !visited[pc+1][pr] ) {
            chi[cl][0] = pc+1, chi[cl][1] = pr, chi[cl][2] = t+1, cl++;
            visited[pc+1][pr] = true;
        }
        if( pr-1 >= 0 && ( brd[pc][pr-1] == '.' || brd[pc][pr-1] == 'D' ) && !visited[pc][pr-1] ) {
            chi[cl][0] = pc, chi[cl][1] = pr-1, chi[cl][2] = t+1, cl++;
            visited[pc][pr-1] = true;
        }
        if( pr+1 < C && ( brd[pc][pr+1] == '.' || brd[pc][pr+1] == 'D' ) && !visited[pc][pr+1] ) {
            chi[cl][0] = pc, chi[cl][1] = pr+1, chi[cl][2] = t+1, cl++;
            visited[pc][pr+1] = true;
        }
        cs++;
    }

    if( esc ) cout << chi[cs][2] << endl;
    else      cout << "KAKTUS" << endl;
}
