#include <iostream>
#include <algorithm>

using namespace std;

long long flst[41];

long long fib( int N ) {
    if( N == 0 ) return 0;
    if( N == 1 ) return 1;
    if( flst[N] == -1 ) flst[N] = fib( N-1 ) + fib( N-2 );
    return flst[N];
}

long long fib0( int N ) {
    if( N == 0 ) return 1;
    return fib( N-1 );
}

long long fib1( int N ) {
    return fib( N );
}

int main() {
    int nc = 0;
    cin >> nc;
    fill( flst, flst+41, -1 );
    for( int cs = 0; cs < nc; ++cs ) {
        int N = 0;
        cin >> N;
        cout << fib0( N ) << ' ' << fib1( N ) << endl;
    }
}
