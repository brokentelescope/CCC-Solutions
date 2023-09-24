#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int mm = 2e6+6;

ll n, c, a[mm], freq[mm/2], total;

ll nCr(ll n, ll r) {
    return n*(n-1)/r;

}
int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> n >> c;

    for (int x = 1; x <= n; x++) {
        cin >> a[x];
        freq[a[x]] ++;
    }

    sort(a+1, a+1+n);

    for (int x = 1; x <= n; x++) a[x+n] = a[x]+c;

    total = n*(n-1)*(n-2)/6;

    for (int x = 1, y = 1; x <= n; x++) {
        while (y <= 2*n && a[y] - a[x] <= c/2) y++;
        total -= nCr((ll)y-x-1, (ll)2);
    }

    if (c % 2 == 0) {
        for (int x = 0; x < c/2; x++) {
            total += freq[x] * nCr(freq[x+c/2], 2) + freq[x+c/2] * nCr(freq[x], 2);
        }
    }
    
    cout << total << "\n";
}