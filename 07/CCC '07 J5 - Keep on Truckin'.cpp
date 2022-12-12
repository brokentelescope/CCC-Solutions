#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    int a, b, n; cin >> a >> b >> n;

    vector<int> dists = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000};

    for (int x = 0, a; x < n; x++) {
        cin >> a; dists.push_back(a);
    }

    sort(dists.begin(), dists.end());

    

    long ways[7001]; 

    for (int x = 0; x < 7001; x++) ways[x] = 0;

    ways[0] = 1;

    for (int x = 0; x < dists.size()-1; x++) {
        for (int y = x+1; y < dists.size(); y++) {
            int dist = dists[y] - dists[x];
            if (dist <= b && dist >= a) {
                ways[dists[y]] += ways[dists[x]];
            }
        }
    }

    cout << ways[7000];
}