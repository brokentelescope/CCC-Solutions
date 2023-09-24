#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef pair<ll, int> pli;

const int mm = 2e3+3;

int n, m;
vector<array<int, 5>> edges;
vector<array<int, 3>> graph[mm];
ll dist[mm];
bool rem[mm];

ll ans = 0;

ll dijkstra(int src, int end) {
    for (int x = 0; x < mm; x++) dist[x] = 1e15;

    priority_queue<pli, vector<pli>, greater<pli>> q;

    q.push({0, src}); dist[src] = 0;

    while (!q.empty()) {
        int d = q.top().first, node = q.top().second; q.pop();
        if (d > dist[node]) continue;
        for (auto e: graph[node]) {
            int v = e[0], w = e[1], id = e[2];
            if (rem[id]) continue;
            if (dist[v] > dist[node]+w) {
                dist[v] = dist[node]+w;
                q.push({dist[v], v});
            }
        }
    }
    return dist[end];

}
int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> m;

    for (int x = 1; x <= m; x++) {
        rem[x] = false;
        int a, b, w, c; cin >> a >> b >> w >> c;
        ans += c;
        edges.push_back({a, b, w, c, x});
        graph[a].push_back({b, w, x});
        graph[b].push_back({a, w, x});
    }

    sort(edges.begin(), edges.end(), [&](array<int, 5> a, array<int, 5> b) {return a[3] > b[3];});

    for (auto e: edges) {
        int a = e[0], b = e[1], w = e[2], c = e[3], id = e[4];
        rem[id] = true;
        if (dijkstra(a, b) > w) rem[id] = false;
        else ans -= c;
    }
    cout << ans << "\n";
}