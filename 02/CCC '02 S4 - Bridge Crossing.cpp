#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi; 

vector<pi> groups[101][101];
int n, m, arr[101], dp[101][101];
string names[101];

int maxr(int l, int r) {
    int ans = 0;

    for (int x = l; x <= r; x++) ans = max(ans, arr[x]);

    return ans;
}

int main() {
    cin >> m >> n;

    for (int x = 1; x <= n; x++) {
        cin >> names[x];
        cin >> arr[x];
        dp[x][x] = arr[x];
        groups[x][x] = {{x, x}};
    }
    
    for (int len = 1; len < n; len++) {
        for (int a = 1, b = a+len; b <= n; a++, b++) {
            if (len+1 <= m) {
                dp[a][b] = maxr(a, b);
                groups[a][b] = {{a, b}};
            }
            else {
                int ans = 1000000;
                for (int mid = a; mid < b; mid++) {
                    if (dp[a][mid] + dp[mid+1][b] < ans) {
                        groups[a][b].clear();
                        ans = dp[a][mid] + dp[mid+1][b];
                        for (pi x: groups[a][mid]) groups[a][b].push_back(x);
                        for (pi x: groups[mid+1][b]) groups[a][b].push_back(x);
                    }
                    
                }    
                dp[a][b] = ans;
            }
        }
    }

    cout << "Total Time: " << dp[1][n] << endl;
    
    for (pi g: groups[1][n]) {
        int l = g.first, r = g.second;
        
        for (int x = l; x <= r; x++) cout << names[x] << " ";
        cout << endl;
    }
}