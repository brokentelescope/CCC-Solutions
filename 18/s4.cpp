#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int mm = 1e6+6;

int n;

unordered_map<int, ll> dp;

ll solve(ll w) {
    
    if (dp.find(w) != dp.end()) return dp[w];

    ll ans = 0;

    ll start = w, f, end_;

    while (start > 1) {
        f = w/start;
        end_ = w/(f+1);
        ans += (start-end_) * solve(f);
        start = end_;
    }

    return dp[w] = ans;
}

int main() {
    cin >> n;

    dp[1] = 1;

    cout << solve(n) << "\n";

}