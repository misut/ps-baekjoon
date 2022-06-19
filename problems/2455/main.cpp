#include <iostream>

using namespace std;

int search( int dt[4], int stt, int end ) {
    int sum = 0, lsum = 0, rsum = 0;
    for( int i = stt; i <= end; ++i ) {
        sum += dt[i];
    }
    if( stt+1 < end )
        lsum = search( dt, stt+1, end );
    if( stt < end-1 )
        rsum = search( dt, stt, end-1 );
    if( sum < lsum ) sum = lsum;
    if( sum < rsum ) sum = rsum;
    return sum;
}

int main() {
    int train[4][2] = {0, };
    int delta[4] = {0, };
    for( int c = 0; c < 4; ++c ) {
        cin >> train[c][0] >> train[c][1];
        delta[c] = train[c][1] - train[c][0];
    }
    cout << search( delta, 0, 3 );
}
