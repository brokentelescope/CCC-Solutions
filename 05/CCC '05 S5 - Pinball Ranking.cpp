#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

const int mm = 1e5+5;

int n, a[mm], bit[mm];
map<int, int> mp;
ld ans = 0;

// idea is to sort the scores, assign each score a rank from 1 to n 
// then use binary indexed tree to see how many values are below a[x]
// query(n) returns how many ranks below n there are 

void update(int idx, int val) {
    for (int x = idx; x < mm; x += x & -x) {
        bit[x] += val;
    }
}

int query(int idx) {
    int ans = 0;
    
    for (int x = idx; x >= 1; x -= x & -x) {
        ans += bit[x];
    }
    
    return ans;
    
}
int main() {
    cin.sync_with_stdio(0); cin.tie(0); 
    
    cin >> n;
    
    for (int x = 1; x <= n; x++) {
        cin >> a[x]; mp[a[x]] = -1;
    }
    
    int rank = 1;
    for (auto &e: mp) {
        e.second = rank;
        rank++;
    }
    
    for (int x = 1; x <= n; x++) {
        ans += (x-query(mp[a[x]]));
        update(mp[a[x]], 1);
    }
    
    cout << setprecision(8) << ans/(ld)n << '\n';
    
}
