#include <bits/stdc++.h>

using namespace std;

set<int> pre, cur;
int r, c, board[100]; 

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> r >> c;

    for (int x = 1; x <= r; x++) {
        string n;
        for (int y = 1; y <= c; y++) {
            char a; cin >> a; n = n + a;
        }
        board[x] = stoi(n, nullptr, 2);
    }

    pre.insert(board[1]);

    for (int x = 2; x <= r; x++) {
        cur.insert(board[x]);

        for (int p: pre) cur.insert(board[x] ^ p);

        pre.clear();

        for (int p: cur) pre.insert(p);
        cur.clear();
    }

    cout << pre.size();

}