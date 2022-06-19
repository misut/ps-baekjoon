#include <iostream>
#include <string>

using namespace std;

char lt[4] = {'D', 'S', 'L', 'R'};
int nc;

string DSLR( int src, int dst ) {
    int stt = 0, end = 1;
    string min( "" );
    bool visited[10000] = {0, };
    int nums[10000] = {0, };
    string insts[10000];
    nums[stt] = src;
    insts[stt] = "";
    visited[src] = true;
    while( end-stt ) {
        int n = nums[stt];
        if( n == dst ) {
            if( !min.size() || min.size() > insts[stt].size() )
                min = insts[stt];
        }
        else {
            int candi[4];
            candi[0] = (nums[stt]*2)%10000;
            candi[1] = nums[stt]==0 ? 9999 : nums[stt]-1;
            candi[2] = (nums[stt]%1000)*10 + nums[stt]/1000;
            candi[3] = nums[stt]/10 + (nums[stt]%10)*1000;
            for( int i = 0; i < 4; ++i ) {
                if( !visited[candi[i]] ) {
                    nums[end] = candi[i];
                    insts[end] = insts[stt];
                    insts[end].push_back( lt[i] );
                    visited[candi[i]] = true;
                    end++;
                }
            }
        }
        stt++;
    }
    return min;
}

int main() {
    int src, dst;
    cin >> nc;
    for( int cs = 0; cs < nc; ++cs ) {
        cin >> src >> dst;
        cout << DSLR( src, dst ) << endl;
    }
}
