#include <bits/stdc++.h>

using namespace std;

const int mm = 1e5+1;
int parent[mm]; 

int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]); 
    }
    return parent[x];
}

void unionn(int x, int y) {
    int xx = find(x); int yy = find(y);
    parent[xx] = yy;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    int g, p; cin >> g >> p;

    for (int x = 0; x < mm; x++) parent[x] = x;

    int cnt = 0;

    for (int x = 0; x < p; x++) {
        int plane; cin >> plane;
        plane = find(plane);
        if (plane == 0) {
            break;
        }
        unionn(plane, plane-1);
        cnt ++;
    }
    cout << cnt;
}   
