// trivial

#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    int n, m; cin >> n >> m;

    char g[n+1][m+1];
    bool vis[n+1][m+1];

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> g[i][j];
            vis[i][j] = 0;
        }
    }

    int r1, c1; cin >> r1 >> c1;
    r1 ++; c1 ++;
    vector<pi> q;

    q.push_back({r1, c1});
    vis[r1][c1] = 1;
    int ans = 0;
    while (!q.empty()) {
        int r = q.back().first, c = q.back().second; q.pop_back();
        if (g[r][c] == 'S') ans += 1;
        if (g[r][c] == 'M') ans += 5;
        if (g[r][c] == 'L') ans += 10;

        for (int addr = -1; addr <= 1; addr++) {
            for (int addc = -1; addc <= 1; addc++) {
                if (addr*addc != 0) continue;
                int newr = r+addr, newc = c+addc;
                if (newr >= 1 && newr <= n && newc >= 1 && newc <= m) {
                    if (!vis[newr][newc] && g[newr][newc] != '*') {
                        vis[newr][newc] = 1;
                        q.push_back({newr, newc});
                    }
                }
            }
        }
    }
    cout << ans << "\n";
}