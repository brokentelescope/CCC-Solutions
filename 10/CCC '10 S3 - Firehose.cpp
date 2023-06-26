#include <bits/stdc++.h>

using namespace std;

const int mm = 1001;

int h, k;
int houses[mm];
bool vis[mm];

int dist(int x,int y){
  return min(y-x, 1000000-y+x);
}

int check(int l) {
    for (int x = 0; x < mm; x++) vis[x] = false;

    int hoses_left = k;

    for (int x = 0; x < h; x++) {
        if (vis[x]) continue;
        // put a hose l units away from current house
        // greedy idea: put it as far away as possible

        if (hoses_left <= 0) return false;
        hoses_left --;

        for (int y = 0; y < h; y++) {
            if (dist(houses[x], houses[y]) <= 2*l) vis[y] = true;
        }
    }
    return true;

}

int main() {
    cin.sync_with_stdio(0); cin.tie(0); 
    cin >> h;
    for (int x = 0; x < h; x++) {
        cin >> houses[x];
    }   
    sort(houses, houses + h);
    cin >> k;

    // binary search approach: if one hose length works
    // we know and longer lengths also work
    // so we only need to consider smaller ones
    // cut search range in half each time
    int ans = 1e6;
    int l = 0, r = 1e6;

    while (l <= r) {
        int mid = (l+r)/2;
        
        if (check(mid)) {
            ans = mid;
            r = mid-1;
        }
        else {
            l = mid+1;
        }
    }
    cout << ans << "\n";
}