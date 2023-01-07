#include <bits/stdc++.h>

using namespace std;

const int inf = numeric_limits<int>::max();

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    string line; getline(cin, line);

    int l = 0, m = 0, s = 0;

    for (int x = 0; x < line.length(); x++) {
        l += line[x] == 'L';
        m += line[x] == 'M';
        s += line[x] == 'S';
    }

    // the idea here is to first break the problem down to only L's and M's first
    // first split the shelf into L, M, and S sections
    // ex. LMS MSLMSM MML --> LLL MMMMMM SSS
    // the S section can be disregarded

    // count how many M's are in the L section 
    // also count how many books aren't L's in the L section
    int M_in_L = 0, notL_in_L = 0;

    for (int x = 0; x < l; x++) {
        M_in_L += line[x] == 'M';
        notL_in_L += line[x] != 'L';
    }

    // count how many L's are in the M section 
    // also count how many books aren't M's in the M section

    int L_in_M = 0, notM_in_M = 0;

    for (int x = l; x < l+m; x++) {
        L_in_M += line[x] == 'L';
        notL_in_L += line[x] != 'M';
    }

    // we can use the minimum of L's in M section and M's in L section to 'solve' at least one of the sections

    cout << notM_in_M + notL_in_L - (min(L_in_M, M_in_L)); 

    
}