#include <iostream>

using namespace std;

int ott( int N ) {
    static int max[11] = {0, 1, 2, 4, };
    if( !max[N] )
        max[N] = ott( N-1 ) + ott( N-2 ) + ott( N-3 );
    return max[N];
}

int main() {
    int nc;
    cin >> nc;
    for(int cs = 0; cs < nc; ++cs ) {
        int N;
        cin >> N;
        cout << ott( N ) << endl;
    }
}
