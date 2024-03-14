#include <bits/stdc++.h>

using namespace std;

const int mm = 1e6+6;
int n, a[mm];

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    int ans = 0;
    for (int i = 1; i <= n/2; i++) {
        if (a[i] == a[i+n/2]) ans += 2;
    }
    cout << ans << "\n";
}