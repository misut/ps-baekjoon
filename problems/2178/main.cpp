#include <iostream>
#include <algorithm>
#include <deque>
#include <tuple>
#include <vector>

using namespace std;

int N = 0, M = 0;
bool pbrd[100][100] = {0, };
int brd[100][100] = {0, };

/* DFS
int lookup_path( int arr[100][100], int sc, int sr, int dc, int dr ) {
    int min = -1;
    int candi[4] = {0, };
    if( sc == dc && sr == dr ) return 1;
    pbrd[sc][sr] = true;
    if( sc-1 >=0 && arr[sc-1][sr] && !pbrd[sc-1][sr] ) candi[0] = lookup_path( arr, sc-1, sr, dc, dr );
    if( sc+1 < N && arr[sc+1][sr] && !pbrd[sc+1][sr] ) candi[1] = lookup_path( arr, sc+1, sr, dc, dr );
    if( sr-1 >=0 && arr[sc][sr-1] && !pbrd[sc][sr-1] ) candi[2] = lookup_path( arr, sc, sr-1, dc, dr );
    if( sr+1 < M && arr[sc][sr+1] && !pbrd[sc][sr+1] ) candi[3] = lookup_path( arr, sc, sr+1, dc, dr );
    pbrd[sc][sr] = false;
    sort( candi, candi+4 );
    for( int i = 0; i < 4; ++i ) {
        if( candi[i] > 0 ) {
            min = candi[i];
            break;
        }
    }
    return min + 1;
}
*/

// BFS
int lookup_path( int arr[100][100], char sc, char sr, char dc, char dr ) {
    int min = 0;
    deque<vector<tuple<char, char>>> works;
    vector<tuple<char, char>> path;
    pbrd[sc][sr] = true;
    path.push_back( make_tuple( sc, sr ) );
    works.push_back( path );
    while( works.size() ) {
        vector<tuple<char, char>>& cur = works[0];
        tuple<char, char>& cp = cur[cur.size()-1];
        vector<tuple<char, char>> ucur, dcur, lcur, rcur;
        tuple<char, char> up, dp, lp, rp;
        char pc = get<0>( cp ), pr = get<1>( cp );
        if( pc == dc && pr == dr ) {
            if( !min || min > cur.size() ) min = cur.size();
        }
        else {
            if( pc-1 >=0 && arr[pc-1][pr] && find( cur.begin(), cur.end(), (up = make_tuple( pc-1, pr )) ) == cur.end() && !pbrd[pc-1][pr] ) {
                for( auto tp : cur ) ucur.push_back( tp );
                pbrd[pc-1][pr] = true;
                ucur.push_back( up );
                works.push_back( ucur );
            }
            if( pc+1 < N && arr[pc+1][pr] && find( cur.begin(), cur.end(), (dp = make_tuple( pc+1, pr )) ) == cur.end() && !pbrd[pc+1][pr] ) {
                for( auto tp : cur ) dcur.push_back( tp );
                pbrd[pc+1][pr] = true;
                dcur.push_back( dp );
                works.push_back( dcur );
            }
            if( pr-1 >=0 && arr[pc][pr-1] && find( cur.begin(), cur.end(), (lp = make_tuple( pc, pr-1 )) ) == cur.end() && !pbrd[pc][pr-1] ) {
                for( auto tp : cur ) lcur.push_back( tp );
                pbrd[pc][pr-1] = true;
                lcur.push_back( lp );
                works.push_back( lcur );
            }
            if( pr+1 < M && arr[pc][pr+1] && find( cur.begin(), cur.end(), (rp = make_tuple( pc, pr+1 )) ) == cur.end() && !pbrd[pc][pr+1] ) {
                for( auto tp : cur ) rcur.push_back( tp );
                pbrd[pc][pr+1] = true;
                rcur.push_back( rp );
                works.push_back( rcur );
            }
        }
        works.pop_front();
    }
    return min;
}

int main() {
    char row[101] = "";
    cin >> N >> M;
    for( int i = 0; i < N; ++i ) {
        cin >> row;
        for( int j = 0; j < M; ++j ) {
            brd[i][j] = row[j] - '0';
        }
    }
    cout << lookup_path( brd, 0, 0, N-1, M-1 );
}
