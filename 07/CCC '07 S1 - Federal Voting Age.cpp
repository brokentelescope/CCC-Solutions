#include <bits/stdc++.h>

using namespace std;

string solve(int y, int m, int d) {
    if (y < 1989) return "Yes"; 
    if (y > 1989) return "No";
    if (m < 2) return "Yes";
    if (m > 2) return "No";
    if (d <= 27) return "Yes";
    return "No";
} 
int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    int n; cin >> n;

    for (int x = 0, a, b, c; x < n; x++) {
        cin >> a >> b >> c;
        cout << solve(a, b, c) << endl;
    }   
}