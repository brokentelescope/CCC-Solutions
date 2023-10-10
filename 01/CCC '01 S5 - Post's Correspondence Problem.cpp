// pure brute force solution 
// almost tle's in c++ kekw

#include <bits/stdc++.h>

using namespace std;

int n, m;

string a[88], b[88];

bool check(vector<int> path) {
    string as, bs;

    for (int x: path) {
        as += a[x]; bs += b[x];
    }

    return (as == bs && as.length());

}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> m >> n;

    for (int x = 1; x <= n; x++) cin >> a[x];
    for (int x = 1; x <= n; x++) cin >> b[x];

    vector<vector<int>> q;

    q.push_back({});

    vector<int> ans = {-1};

    while (!q.empty()) {
        vector<int> cur = q.back(); q.pop_back();

        if (check(cur)) {
            ans = cur; 
            break;
        }

        if (cur.size() == m) continue;

        for (int x = 1; x <= n; x++) {
            cur.push_back(x);
            q.push_back(cur);
            cur.pop_back();
        }
    }

    if (ans[0] == -1) cout << "No solution.\n";
    else {
        cout << ans.size() << "\n";
        for (int x: ans) cout << x << "\n";
    }
    

}