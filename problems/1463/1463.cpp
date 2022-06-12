#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int make_one( int X ) {
    bool late[1000000] = {0, };
    deque<vector<int>> xq;
    xq.push_back( vector<int>( {X, 0} ) );
    late[0] = true;
    while( xq.size() ) {
        int cx = xq[0][0], ct = xq[0][1], cnd;
        vector<int> A, B, C;
        if( cx == 1 ) break;
        if( cx%3 == 0 && !late[cnd=cx/3] ) {
            A.push_back( cnd );
            A.push_back( ct+1 );
            xq.push_back( A );
            late[cnd] = true;
        }
        if( cx%2 == 0 && !late[cnd=cx/2] ) {
            B.push_back( cnd );
            B.push_back( ct+1 );
            xq.push_back( B );
            late[cnd] = true;
        }
        if( cx > 1 && !late[cnd=cx-1] ) {
            C.push_back( cnd );
            C.push_back( ct+1 );
            xq.push_back( C );
            late[cnd] = true;
        }
        xq.pop_front();
    }
    return xq[0][1];
}

int main() {
    int X;
    cin >> X;
    cout << make_one( X ) << endl;
}
