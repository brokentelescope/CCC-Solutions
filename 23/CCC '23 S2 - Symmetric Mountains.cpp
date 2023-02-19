#include <bits/stdc++.h>

using namespace std;

int arr[5000];

int dp[5000][5000];

int ans[5001];

int n;

const int inf = numeric_limits<int>::max();

int solve(int l, int r) {
    if (dp[l][r] != -1) return dp[l][r];

    if (r - l <= 0) return 0;

    int result = abs(arr[l]-arr[r]) + solve(l+1, r-1);

    dp[l][r] = result;
    ans[r-l+1] = min(ans[r-l+1], result);
    return result;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n; 

    for (int x = 0; x < n; x++) {
        cin >> arr[x];
        ans[x] = inf;
    }
    ans[n] = inf; 
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            dp[x][y] = -1;
        }
    }

    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            solve(x, y);
        }
    }

    cout << 0 << " ";
    for (int x = 2; x <= n; x++) {
        cout << ans[x] << " ";
    }
}