#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    int a[n];
    int freq[2001];
    int pos[4001];

    for (int x = 0; x < 2001; x++) {
        freq[x] = 0;
    }

    for (int x = 0; x < 4001; x++) {
        pos[x] = 0;
    }

    for (int x = 0; x < n; x++) {
        cin >> a[x];
        freq[a[x]]++;
    }

    for (int x = 1; x < 2001; x++) {
        for (int y=x; y < 2001; y++) {
            if (x==y) {
                pos[x+y] += freq[x]/2;
            }

            else {
                pos[x+y] += min(freq[x], freq[y]); 
            }
        }
    }

    int max = 0;
    int cnt = 0;

    for (int x = 1; x < 4001; x++) {
        if (pos[x] > max) {
            max = pos[x];
            cnt = 1; 
        }

        else if (pos[x] == max) {
            cnt ++;
        }
    }

    cout << max << " " << cnt;

}