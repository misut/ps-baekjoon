#include <iostream>

using namespace std;

long long padoban( int N ) {
    static long long memory[101] = {1, 1, 1, 1, 2, 2, };
    if( !memory[N] )
        memory[N] = padoban( N-1 ) + padoban( N-5 );
    return memory[N];
}

int main() {
    int nc = 0;
    cin >> nc;
    for( int cs = 0; cs < nc; ++cs ) {
        int N;
        cin >> N;
        cout << padoban( N ) << endl;
    }
}
