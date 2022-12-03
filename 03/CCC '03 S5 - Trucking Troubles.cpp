#include <bits/stdc++.h>

using namespace std;

const int mm = 1e4+1;

bool vis[mm];
bool dest[mm];
int key[mm];
int n;
vector<pair<int, int>> graph[mm];

int maxkey() {
    int max = 0;
    int mindex;
    for (int x = 0; x <= n; x++) {
        if (key[x] > max && !vis[x]) {
            max = key[x];
            mindex = x;
        }
    }
    return mindex;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    int m, d; cin >> n >> m >> d;

    for (int x = 0; x < mm; x++) {
        key[x] = 0; vis[x] = false; dest[x] = false;
    }

    for (int x = 0; x < m; x++) {
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back({c, b}); 
        graph[b].push_back({c, a}); 
    }
    
    for (int x = 0, a; x < d; x++) {
        cin >> a; dest[a] = true;
    }

    key[1] = numeric_limits<int>::max();

    for (int x = 0 ; x < n; x++) {
        int node = maxkey();
        vis[node] = true;
        for (pair<int, int> next: graph[node]) {
            if (!vis[next.second] && key[next.second] < next.first) {
                key[next.second] = next.first;
            }
        }
    }

    int max = numeric_limits<int>::max(); 

    for (int x = 1; x <= n; x++) { 
        if (dest[x]) {
            max = min(max, key[x]);
        }
    }
    cout << max;
}
