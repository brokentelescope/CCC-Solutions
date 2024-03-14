#include <bits/stdc++.h>

using namespace std;

const int mm = 2e5+5;

typedef pair<int, int> pi;

vector<pi> graph[mm];

int n, m, vis[mm];
char ans[mm];

void dfs(int node, char prv) {
    for (auto edge: graph[node]) {
        int v = edge.first, i = edge.second;
        if (!vis[v]) {
            vis[v] = true;
            if (prv == 'R') ans[i] = 'B';
            else ans[i] = 'R';
            dfs(v, ans[i]);
        }
    }
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        ans[i] = 'G';
        int a, b; cin >> a >> b;
        graph[a].push_back({b, i});
        graph[b].push_back({a, i});
    }

    for (int i = 1; i <= n; i++) {
        if (!vis[i]) {
            vis[i] = true;
            dfs(i, 'B');
        }
    }

    for (int i = 0; i < m; i++) cout << ans[i]; cout << "\n";
}