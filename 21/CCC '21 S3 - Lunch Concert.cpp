#include <bits/stdc++.h>

using namespace std;

const long inf = numeric_limits<long>::max();

const long mm = 2e5+2;

long n;

long pos[mm], speed[mm], range[mm];

long check(long position) {
    long s = 0; 

    long zero = 0;
    for (long x = 0; x < n; x++) {
        s += max(zero, abs(pos[x]-position)-range[x]) * speed[x]; 
    }

    return s;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n; 

    for (long x = 0; x < n; x++) {
        cin >> pos[x] >> speed[x] >> range[x];
    }

    long low = 0, hi = 1e9;

    long mid_score = 0;

    while (low <= hi) {
        long mid = (low+hi)/2;

        mid_score = check(mid);
        long left_score = check(mid-1);
        long right_score = check(mid+1);

        if (mid_score == left_score || mid_score == right_score) break;
        else if (mid_score < left_score && mid_score < right_score) break;
        else if (mid_score < right_score) hi = mid - 1;
        else low = mid + 1;
    }

    cout << mid_score;
}