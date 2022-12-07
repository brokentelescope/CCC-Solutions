#include <bits/stdc++.h>

using namespace std;

string solve() {
    string a, b, c; cin >> a >> b >> c;
    int ab = a.length()-b.length();
    int ac = a.length()-c.length();
    int ba = b.length()-a.length();
    int bc = b.length()-c.length();
    int ca = c.length()-a.length();
    int cb = c.length()-b.length();

    if (a.find(b) == 0 || a.find(c) == 0) return "No";
    if (b.find(a) == 0 || b.find(c) == 0) return "No";
    if (c.find(b) == 0 || c.find(a) == 0) return "No";
    if (a.find(b) == max(0, ab) || a.find(c) == max(0, ac)) return "No";
    if (b.find(a) == max(0, ba) || b.find(c) == max(0, bc)) return "No";
    if (c.find(a) == max(0, ca) || c.find(b) == max(0, cb)) return "No";

    return "Yes";

}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    int n; cin >> n; 
    for (int x = 0; x < n; x++) cout << solve() << endl;
}