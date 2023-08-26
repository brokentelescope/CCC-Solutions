#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi;

int n, t, p, src;

const int mm = 5e3+3;

vector<pi> graph[mm];

int pencil[mm], dist[mm], vis[mm];

int minNode() {
    int min_val = 1e9;
    int node = -1;

    for (int x = 1; x <= n; x++) {
        if (dist[x] < min_val && !vis[x]) {
            min_val = dist[x];
            node = x;
        }
    }
    return node;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> t;

    for (int x = 0; x < t; x++) {
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    for (int x = 1; x <= n; x++) {
        pencil[x] = 1e9;
        dist[x] = 1e9;
        vis[x] = false;
    }

    cin >> p;

    for (int x = 0; x < p; x++) {
        int a, b; cin >> a >> b;
        pencil[a] = b;
    }

    cin >> src;

    // run dijkstra

    dist[src] = 0;

    for (int x = 0; x < n; x++) {
        // find min node
        int node = minNode(); vis[node] = true;
        // update neighbours
        for (pi edge: graph[node]) {
            int v = edge.first, w = edge.second;
            dist[v] = min(dist[v], dist[node] + w);
        }
    }

    int ans = 1e9;

    for (int x = 1; x <= n; x++) ans = min(ans, dist[x] + pencil[x]);
    
    cout << ans << "\n";
}