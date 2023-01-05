#include <bits/stdc++.h>

using namespace std;

const int mm = 2002;

vector<vector<int>> graph[mm]; 

const int inf = numeric_limits<int>::max();
int dist[mm][202];

int k, n, m; 

int dijkstra(int src, int end) {

    for (int x = 0; x < mm; x++) 
        for (int y = 0; y < 202; y++) 
            dist[x][y] = inf;
    

    dist[src][0] = 0;

    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;

    pq.push({0, 0, src});

    int mintime = inf;

    while (!pq.empty()) {
        int d = pq.top()[0];
        int rock = pq.top()[1];
        int node = pq.top()[2];

        pq.pop();

        if (node == end) mintime = min(mintime, d);

        if (d >= mintime || rock >= k) continue;

        for (vector<int> x: graph[node]) {
            int v = x[0], time = x[1], wear = x[2];

            if (rock + wear < k ) {
                if (dist[v][rock+wear] > dist[node][rock] + time) {
                    dist[v][rock+wear] = dist[node][rock] + time;
                    pq.push({dist[node][rock] + time, rock+wear, v});
                }
            }
        }
    }
    if (mintime == inf) return -1;
    return mintime;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> k >> n >> m; 

    for (int x = 0; x < m; x++) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        graph[a].push_back({b, c, d});
        graph[b].push_back({a, c, d});
    }

    int a, b; cin >> a >> b;

    cout << dijkstra(a, b);
}