// Dynamic Programming approach

#include <bits/stdc++.h>

using namespace std;

const int inf = numeric_limits<int>::max();

int clubs[100];
int dist[6000];

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    int d, c; cin >> d >> c;


    for (int x = 0; x < c; x++) cin >> clubs[x];

    for (int x = 0; x < 5281; x++) dist[x] = inf;

    dist[0] = 0;

    for (int x = 0; x < d; x++) {
        if (dist[x] == inf) continue;
        for (int y = 0; y < c; y++) {
            dist[x+clubs[y]] = min(dist[x+clubs[y]], dist[x]+1);
        }
    }

    if (dist[d] == inf) cout << "Roberta acknowledges defeat.";
    else cout << "Roberta wins in " << dist[d] << " strokes.";


}
