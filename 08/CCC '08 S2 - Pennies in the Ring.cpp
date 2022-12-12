#include <bits/stdc++.h>

using namespace std;

int solve(int n) {
    int cnt = 0; 

    for (int x = 1; x <= n; x++) {
        cnt += sqrt(n*n-x*x); cnt ++;
    }

    return cnt*4+1;
}


int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    while (true) {
        int a; cin >> a;
        if (a == 0) break;
        cout << solve(a) << endl;
    }

}