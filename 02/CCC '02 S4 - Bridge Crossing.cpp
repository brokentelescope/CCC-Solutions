#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi; 

vector<pi> groups[101][101];
int n, m, arr[101], dp[101][101];

// dp[x][y] represents the shortest time needed for people x -> y (inclusive) to cross
// groups[x][y] represents the splits needed to get the best time
// for example groups[1][n] = [(1, 1), (2, 3), (4, 5)] for the sample input
// group 1 is 1
// group 2 is 2, 3
// group 3 is 4, 5

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
        // base case the best time for the people from x -> x to cross is just the amount of time it takes x to cross
        dp[x][x] = arr[x];
        groups[x][x] = {{x, x}};
    }

    // loop through group sizes starting from 2, since we already know the answer for sizes of group 1
    for (int len = 1; len < n; len++) {
        for (int a = 1, b = a+len; b <= n; a++, b++) {
            // if the group size is less than equal to m, 
            // the time needed is simply the maximum crossing time of any individual in the group
            if (len+1 <= m) {
                dp[a][b] = maxr(a, b);
                groups[a][b] = {{a, b}};
            }
            else {
                // if the group size is more than m,
                // we need to split the group somehow
                int ans = 1000000;
                for (int mid = a; mid < b; mid++) {
                    // lets say the group size is 4, a = 1, b = 4
                    // 1 | 2 | 3 | 4
                    // we can split it at each '|'
                    // the best time is the sum of the crossing times of the two groups
                    // loop through each split point to find the best answer
                    
                    if (dp[a][mid] + dp[mid+1][b] < ans) {
                        // if we found a better solution keep track of the group 
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
