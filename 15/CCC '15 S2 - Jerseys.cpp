#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int j, a; 
    cin >> j >> a;

    int sizes[j+1];

    for (int x = 1; x <= j; x++) {
        char a; 
        cin >> a;
        sizes[x] = int(a);
    } 

    int cnt = 0;
    for (int x = 0; x < a; x++) { 
        int num, size; char a; 
        cin >> a >> num;
        size = int(a);

        if (sizes[num] <= size) {
            cnt ++; 
            sizes[num] = 1000;
        } 
        
        
    }
    cout << cnt;
}