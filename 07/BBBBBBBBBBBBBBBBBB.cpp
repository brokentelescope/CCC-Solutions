#include <bits/stdc++.h>

using namespace std;

const int mm = 3e4+4;

int n, w, k, a[mm], psa[mm], dp[mm][505];

int sum(int a, int b) {
    return psa[b] - psa[a-1];
}

int f(int i, int b) {

    if (i > n) return 0;
    if (b <= 0) return 0;

    if (dp[i][b] != -1) return dp[i][b];

    int a = f(i+w, b-1) + sum(i, i+w-1);
    int c = f(i+1, b);

    return dp[i][b] = max(a, c);
}

void solve() {
    cin >> n >> k >> w;

    for (int x = 0; x <= n; x++) {
        for (int y = 0; y <= k; y++) {
            dp[x][y] = -1;
        }
    }

    psa[0] = 0; 
    for (int x = 1; x <= n; x++) {
        cin >> a[x];
        psa[x] = psa[x-1] + a[x];
    }

    cout << f(1, k) << "\n";
}
int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    int t; cin >> t;

    for (int x = 0; x < t; x++) {
        solve();
    }
}