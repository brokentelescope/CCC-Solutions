#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);   

    int p, n, r; cin >> p >> n >> r;

    int last = n;
    int cnt = 0;
    
    while(n <= p) {
        n += last * r; 
        last *= r; 
        cnt ++;
    }
    
    cout << cnt;
    
}
