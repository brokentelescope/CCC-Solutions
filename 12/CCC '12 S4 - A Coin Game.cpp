#include <bits/stdc++.h>

using namespace std;

const int mm = 1<<21+1;

bool vis[mm];

int top[7];

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    while (true) {
        int n; cin >> n;
        if (n == 0) break;

        for (int x = 0; x < mm; x++) vis[x] = false;

        queue<int> q;

        int mask = 0;
        // compress the starting state into a bitmask
        for (int x = 0; x < n; x++) {
            int a; cin >> a; a--;
            mask = mask | (x << (3*a));
        }
        
        int end = 0;

        for (int x = 0; x < n; x++) {
            end = end | (x << 3*x);
        }

        q.push(mask); 

        int cnt = 0;

        bool flag = true;
        while (!q.empty() && flag) {
            int s = q.size();
            for (int x = 0; x < s; x++) {
                int node = q.front(); q.pop();

                if (node == end) {
                    flag = false;
                    cout << cnt << "\n";
                    break;
                }
                for (int x = 0; x < n; x++) top[x] = 10;
                // loop through the mask
                for (int x = 0; x < n; x++) {
                    top[(node >> x*3) & 7] = min(top[(node >> x*3) & 7], x);
                }

                for (int x = 0; x < n; x++) {
                    // checking coin x
                    // 0 --> 1 --> 2
                    int pos = (node >> x*3) & 7;

                    // check if coin x is the top of its stack
                    if (top[pos] == x) {
                        // move left: we can't be at the leftmost position
                        if (pos != 0) {
                            if (top[pos - 1] > x) {
                                // move coin x to the left by 1

                                int left = ((node >> (x*3))-1) << (x*3);

                                int right = ((1 << (3*x))-1) & node;

                                int next = left | right;
                                
                                if (!vis[next]) {
                                    q.push(next);
                                    vis[next] = true;
                                }

                            }
                        }
                        // move right: we can't be at the rightmost position
                        if (pos != n-1) {
                            if (top[pos + 1] > x) {
                                // move coin x to the right by 1
                                int left = ((node >> (x*3))+1) << (x*3);

                                int right = ((1 << (3*x))-1) & node;

                                int next = left | right;

                                if (!vis[next]) {
                                    q.push(next);
                                    vis[next] = true;
                                }
                            }
                        }
                    }
                }      


            }
            cnt ++;
        }
        if (flag) {
            cout << "IMPOSSIBLE\n";
        }
    }
}
