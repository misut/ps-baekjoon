#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int N, K;
    long long dolls[500] = {0, }, ksums[500] = {0, }, ksqrs[500] = {0, };
    long double min = -1;
    cin >> N >> K;
    for( int i = 0; i < N; ++i )
        cin >> dolls[i];
    for( K; K <= N; ++K ) {
        ksums[K-1] = 0, ksqrs[K-1] = 0;
        for( int i = 0; i < K; ++i ) {
            ksums[K-1] += dolls[i];
            ksqrs[K-1] += dolls[i]*dolls[i];
        }
        for( int i = K; i < N; ++i ) {
            ksums[i] = ksums[i-1] + dolls[i] - dolls[i-K];
            ksqrs[i] = ksqrs[i-1] + dolls[i]*dolls[i] - dolls[i-K]*dolls[i-K];
        }
        for( int i = K-1; i < N; ++i ) {
            long double sqr_avg = (long double)ksums[i] / K;
            long double avg_sqr = (long double)ksqrs[i] / K;
            long double candi = avg_sqr - sqr_avg*sqr_avg;
            if( min < 0 || min > candi )
                min = candi;
        }
    }
    cout.precision( 11 );
    cout << sqrt( min ) << endl;
}
