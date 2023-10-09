#include <bits/stdc++.h>

using namespace std;

const int mm = 155555;

int n, m, a[mm], dif[17][mm];
int l[mm], r[mm], v[mm];
int st[mm][20];

int gcd(int x, int y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}

int lcm(int x, int y) {
    return x*y/gcd(x, y);
}

int query(int l, int r) {
    int m = log2(r-l+1);
    return gcd(st[l][m], st[r - (1 << m) + 1][m]);
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> m;

    // make dif array updates
    for (int x = 1; x <= m; x++) {
        cin >> l[x] >> r[x] >> v[x];
        dif[v[x]][l[x]] ++;
        dif[v[x]][r[x]+1] --;
    }

    // build dif arrays
    for (int x = 1; x <= 16; x++) {
        dif[x][0] = 0;
        for (int y = 1; y <= n; y++) {
            dif[x][y] += dif[x][y-1];
        }
    }

    // build our output array
    for (int x = 1; x <= n; x++) {
        a[x] = 1;
        // put all factors in
        for (int y = 1; y <= 16; y++) {
            if (dif[y][x] > 0) {
                a[x] = lcm(a[x], y);
            }
        }
    }

    // build sparse table

    // base case: st[x][0] = a[x]
    for (int x = 1; x <= n; x++) st[x][0] = a[x];

    // build rest:
    for (int x = 1; (1 << x) <= n; x++) {
        for (int y = 1; (y + (1 << x) - 1) <= n; y++) {
            st[y][x] = gcd(st[y][x-1], st[(y + (1 << (x-1)))][x-1]);
        }
    }

    // check requirements again
    for (int x = 1; x <= m; x++) {
        if (query(l[x], r[x]) != v[x]) {
            cout << "Impossible\n";
            return 0;
        }
    }
    for (int x = 1; x <= n; x++) cout << a[x] << " ";
}