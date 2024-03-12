#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

ld x0, y0, z0, xs, ys, zs, x, y, z, d, ans;

char dir;
ld dist(ld x1, ld y1, ld z1, ld x2, ld y2, ld z2) {
    return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1));
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> xs >> ys >> zs >> x0 >> y0 >> z0;

    x = 1, y = 0, z = 0;
    
    ans = dist(xs, ys, zs, x0, y0, z0);

    while (true) {
        cin >> d >> dir;
        if (dir == 'E') {
            cout << ans; return 0;
        }

        xs += (d*x);
        ys += (d*y);
        zs += (d*z);

        if ()
    }
}