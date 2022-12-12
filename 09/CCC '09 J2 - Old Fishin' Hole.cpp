#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);   

    int trout, pike, pickerel, n; cin >> trout >> pike >> pickerel >> n;

    int cnt = 0; 
    for (int t = 0; t <= n/trout; t++) {
        for (int p = 0; p <= n/pike; p++) {
            for (int pic = 0; pic <= n/pickerel; pic++) {
                if (t*trout + p*pike + pic*pickerel <= n && t*trout + p*pike + pic*pickerel != 0) {
                    cnt ++; 
                    cout << t << " Brown Trout, " << p << " Northern Pike, " << pic << " Yellow Pickerel" << endl; 
                }
            }
        }
    } 

    cout << "Number of ways to catch fish: " << cnt;
}