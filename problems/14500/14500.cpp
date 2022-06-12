#include <iostream>
#include <set>
#include <tuple>

using namespace std;

int C, R;

int search( int brd[500][500] ) {
    int max = 0;
    set<tuple<int, int>> tet;
    for( int c = 0; c < C; ++c ) {
        for( int r = 0; r < R; ++r ) {
            int tmp=brd[c][r];
            tet.clear();
            tet.insert( make_tuple( c, r ) );
            for( int t = 0; t < 3; ++t ) {
                int pmax = 0;
                tuple<int, int> pnt;
                for( auto& p : tet ) {
                    int x = get<0>( p ), y = get<1>( p );
                    if( x-1>=0 && tet.find( make_tuple( x-1, y ) ) == tet.end() && pmax < brd[x-1][y] )
                        pmax = brd[x-1][y], pnt = make_tuple( x-1, y );
                    if( x+1< C && tet.find( make_tuple( x+1, y ) ) == tet.end() && pmax < brd[x+1][y] )
                        pmax = brd[x+1][y], pnt = make_tuple( x+1, y );
                    if( y-1>=0 && tet.find( make_tuple( x, y-1 ) ) == tet.end() && pmax < brd[x][y-1] )
                        pmax = brd[x][y-1], pnt = make_tuple( x, y-1 );
                    if( y+1< R && tet.find( make_tuple( x, y+1 ) ) == tet.end() && pmax < brd[x][y+1] )
                        pmax = brd[x][y+1], pnt = make_tuple( x, y+1 );
                }
                tet.insert( pnt );
                tmp += pmax;
            }
            max = max<tmp ? tmp : max;
        }
    }
    return max;
}

int main() {
    int brd[500][500];
    cin >> C >> R;
    for( int c = 0; c < C; ++c )
        for( int r = 0; r < R; ++r )
            cin >> brd[c][r];
    cout << search( brd ) << endl;
}
