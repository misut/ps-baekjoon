#include <iostream>

using namespace std;

int getmax( int* stt, const int* end ) {
    int max = 0b10000000'00000000'00000000'00000000;
    for( stt; stt != end; ++stt )
        if( max < *stt ) max = *stt;
    return max;
}

int main() {
    int N;
    int tri[501][501] = {0, };
    cin >> N;
    for( int c = 1; c <= N; ++c ) {
        for( int r = 1; r <= c; ++r ) {
            cin >> tri[c][r];
            tri[c][r] += tri[c-1][r-1] > tri[c-1][r] ? tri[c-1][r-1] : tri[c-1][r];
        }
    }
    cout << getmax( tri[N], tri[N]+N+1 );
}
