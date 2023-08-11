#include <bits/stdc++.h>

using namespace std;

const int mm = 2e3+3;

typedef long long ll;

struct piece {
    int l;
    int r;
    int top;
    int bot;
    int v;
};

int n, t, dif[mm][mm];
ll ans;
piece arr[mm];

map<int, int> xcords, ycords;

vector<int> realx, realy;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> t;
    
    for (int x = 0; x < mm; x++) {
        for (int y = 0; y < mm; y++) {
            dif[x][y] = 0;
        }
    }

    for (int x = 1; x <= n; x++) {
        cin >> arr[x].l >> arr[x].top >> arr[x].r >> arr[x].bot >> arr[x].v;
        xcords[arr[x].l] = xcords[arr[x].r] = ycords[arr[x].top] = ycords[arr[x].bot] = -1;
    }

    int cnt = 1;

    for (auto &cord: xcords) {cord.second = cnt; realx.push_back(cord.first); cnt ++;}

    cnt = 1;

    for (auto &cord: ycords) {cord.second = cnt; realy.push_back(cord.first); cnt ++;}

    for (int x = 1; x <= n; x++) {
        int x1 = xcords[arr[x].l], x2 = xcords[arr[x].r];
        int y1 = ycords[arr[x].top], y2 = ycords[arr[x].bot];

        dif[x1][y1] += arr[x].v; dif[x2][y2] += arr[x].v;
        dif[x1][y2] -= arr[x].v; dif[x2][y1] -= arr[x].v;
    }

    for (int x = 1; x < xcords.size(); x++) {
        for (int y = 1; y < ycords.size(); y++) {
            dif[x][y] += dif[x-1][y] + dif[x][y-1] - dif[x-1][y-1];
            if (dif[x][y] >= t) {
                ans += (ll)(realx[x] - realx[x-1])*(ll)(realy[y] - realy[y-1]);
            }
        }
    }
    cout << ans << "\n";
}