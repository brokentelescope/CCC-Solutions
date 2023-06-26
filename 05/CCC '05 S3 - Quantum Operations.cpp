#include <bits/stdc++.h>

using namespace std;

const int mm = 1024;

int a[mm][mm], b[mm][mm], ans[mm][mm];
int n, r, c, r2, c2;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);   

    cin >> n;

    // read initial array
    cin >> r >> c;

    for (int x = 0; x < r; x++) {
        for (int y = 0; y < c; y++) {
            cin >> a[x][y];
        }
    }

    for (int i = 0; i < n-1; i++) {
        // read the second matrix
        cin >> r2 >> c2;
        for (int x = 0; x < r2; x++) {
            for (int y = 0; y < c2; y++) {
                cin >> b[x][y];
            }
        }
        // compute the tensor prod and put it into ans
        for (int x = 0; x < r; x++) {
            for (int y = 0; y < c; y++) {
                int v = a[x][y];
                int posx = x*r2; int posy = y*c2;
                //
                for (int x2 = 0; x2 < r2; x2++) {
                    for (int y2 = 0; y2 < c2; y2++) {
                        ans[posx+x2][posy+y2] = b[x2][y2] * v;
                    }
                }
                //
            }
        }
        // copy the tensor prod back into a
        r = r*r2;
        c = c*c2;

        for (int x = 0; x < r; x++) {
            for (int y = 0; y < c; y++) {
                a[x][y] = ans[x][y];
            }
        }
    }

    // compute the needed values
    int maxElem = -1e9;
    int minElem = 1e9;
    int maxRow = -1e9;
    int minRow = 1e9;
    int maxCol = -1e9;
    int minCol = 1e9;

    for (int x = 0; x < r; x++) {
        for (int y = 0; y < c; y++) {
            maxElem = max(maxElem, a[x][y]);
            minElem = min(minElem, a[x][y]);
        }
    }

    for (int x = 0; x < r; x++) {
        int rowSum = 0;
        for (int y = 0; y < c; y++) {
            rowSum += a[x][y];
        }
        maxRow = max(maxRow, rowSum);
        minRow = min(minRow, rowSum);
    }

    for (int x = 0; x < c; x++) {
        int colSum = 0;
        for (int y = 0; y < r; y++) {
            colSum += a[y][x];
        }
        maxCol = max(maxCol, colSum);
        minCol = min(minCol, colSum);
    }
    
    cout << maxElem << "\n";
    cout << minElem << "\n";
    cout << maxRow << "\n";
    cout << minRow << "\n";
    cout << maxCol << "\n";
    cout << minCol << "\n";
}   
