#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll mm = 3e3+3;

ll n, m, a[mm], b[mm], dp[mm][101][101][2];

ll solve(ll x, ll l, ll r, bool prev) {

    if (dp[x][l][r][prev] != -1) return dp[x][l][r][prev];

    ll ret = 0;
    // if there are still pies from the line left
    if (x <= n) {
        // take current pie from line 
        if (!prev) ret = max(ret, solve(x+1, l, r, true) + a[x]);
        // skip
        ret = max(ret, solve(x+1, l, r, false));
    }
    // use extra bag pies 
    if (l <= r) {
        // use current bag pie as separator
        ret = max(ret, solve(x, l+1, r, false));
        // take current bag pie
        if (!prev) ret = max(ret, solve(x, l, r-1, true) + b[r]);
    }
    return dp[x][l][r][prev] = ret;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n;
    for (ll x = 1; x <= n; x++) cin >> a[x];
    cin >> m;
    for (ll x = 1; x <= m; x++) cin >> b[x];
    sort(b+1, b+1+m);

    memset(dp, -1, sizeof(dp));
    
    cout << solve(1, 1, m, false) << "\n";
}