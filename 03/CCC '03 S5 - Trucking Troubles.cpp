#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi;

const int mm = 2e5+5;
int n, m, d, best[mm];

vector<pi> graph[mm];
priority_queue<pi> q;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> m >> d;

    for (int x = 1; x <= m; x++) {
        best[x] = 0;
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }

    best[1] = 1e9;

    q.push({1e9, 1});

    while (!q.empty()) {
        int node = q.top().second; q.pop();

        for (pi x: graph[node]) {
            int v = x.first, w = x.second;
            if (min(best[node], w) > best[v]) {
                best[v] = min(best[node], w);
                q.push({best[v], v});
            }
        }
    }

    int ans = 1e9;

    for (int x = 0; x < d; x++) {
        int i; cin >> i; 
        ans = min(ans, best[i]);
    }

    cout << ans << "\n";
}