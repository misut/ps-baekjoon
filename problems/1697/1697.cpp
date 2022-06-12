#include <iostream>

using namespace std;

int N, K;

int brother( int src, int dst ) {
    bool visited[100001] = {0, };
    int min = 0;
    int stt = 0, end = 0;
    int plst[100001] = {0, };
    int nlst[100001] = {0, };
    plst[stt] = src;
    visited[src] = true;
    end++;
    while( end-stt ) {
        int pos = plst[stt];
        if( pos == dst ) {
            if( !min || min > nlst[stt] )
                min = nlst[stt];
        }
        else {
            if( pos-1>=0 && !visited[pos-1] ) {
                plst[end] = pos-1;
                nlst[end] = nlst[stt]+1;
                end++;
                visited[pos-1] = true;
            }
            if( pos+1<=100000 && !visited[pos+1] ) {
                plst[end] = pos+1;
                nlst[end] = nlst[stt]+1;
                end++;
                visited[pos+1] = true;
            }
            if( pos*2<=100000 && !visited[pos*2] ) {
                plst[end] = pos*2;
                nlst[end] = nlst[stt]+1;
                end++;
                visited[pos*2] = true;
            }
        }
        stt++;
    }
    return min;
}

int main() {
    cin >> N >> K;
    cout << brother( N, K );
}
