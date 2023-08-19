#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi;

const int mm = 2e5+5;

int n, w, d, perm[mm], time_[mm];

vector<int> graph[mm];

multiset<pi> ms;

// dist[x] --> how long it takes to get from
// node x to node n thru walkways only

int dist[mm];

void bfs(int node) {
    int vis[mm];
    for (int x = 0; x < mm; x++) vis[x] = false;
    vis[node] = true;
    dist[node] = 0;

    queue<int> q;
    q.push(node);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int x: graph[u]) {
            if (!vis[x]) {
                dist[x] = dist[u] + 1;
                q.push(x);
                vis[x] = true;
            }
        }
    }
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> w >> d;

    for (int x = 1; x <= n; x++) dist[x] = 1e7;

    for (int x = 0, a, b; x < w; x++) {
        cin >> a >> b;
        graph[b].push_back(a);
    }

    // run dfs to fill node array
    dist[n] = 0;

    bfs(n); 

    for (int x = 1; x <= n; x++) cin >> perm[x];

    for (int x = 1; x <= n; x++) {
        // get off at stop x
        ms.insert({x-1+dist[perm[x]], perm[x]});
        time_[perm[x]] = x-1+dist[perm[x]];
    }

    for (int x = 0, a, b, c; x < d; x++) {

        cin >> a >> b; 

        time_[perm[a]] = b-1 + dist[perm[a]];
        time_[perm[b]] = a-1 + dist[perm[b]];

        ms.insert({time_[perm[a]], perm[a]});
        ms.insert({time_[perm[b]], perm[b]});
        
        while (true) {
            pi q = *ms.begin();
            int time = q.first, node = q.second;
            if (time != time_[node]) {
                ms.erase(ms.begin()); continue;
            }
            cout << time << "\n";
            break;
        }

        c = perm[a];
        perm[a] = perm[b];
        perm[b] = c;
    }
}