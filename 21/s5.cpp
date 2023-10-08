#include <bits/stdc++.h>

using namespace std;

const int mm = 2e5+5;

int n, m, a[mm], dif[16][mm], l[mm], r[mm], v[mm], st[20][mm];

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int lcm(int a, int b) {
    return a*b/gcd(a,b);
}

int query(int l, int r) {
    int k = log2(r - l  + 1);
    return gcd(st[k][l], st[k][r - (1 << k) + 1]);
}
int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> m;

    for (int x = 1; x <= 16; x++) {
        for (int y = 1; y <= n; y++) {
            dif[x][y] = 0;
        }
    }
    for (int x = 1; x <= m; x++) {
        cin >> l[x] >> r[x] >> v[x];
        dif[v[x]][l[x]] ++;
        dif[v[x]][r[x]+1] --;
    }

    for (int x = 1; x <= n; x++) {
        a[x] = 1;
        for (int y = 1; y <= 16; y++) {
            dif[y][x] += dif[y][x-1];
            if (dif[y][x] > 0) a[x] = lcm(a[x], y);
        }
        st[0][x] = a[x];
    }

    for (int x = 1; x <= log2(n); x++) {
        for (int y = 1; y + (1 << x) - 1 <= n; y++) {
            st[x][y] = gcd(st[x-1][y], st[x-1][y + (1<<x-1)]);
        }
    }

    // for (int x = 1; x <= m; x++) {
    //     if (query(l[x], r[x]) != v[x]) {
    //         cout << "Impossible\n";
    //         return 0;
    //     }
    // }

    for (int x = 1; x <= n; x++) {
        cout << a[x] << " ";
    }

}