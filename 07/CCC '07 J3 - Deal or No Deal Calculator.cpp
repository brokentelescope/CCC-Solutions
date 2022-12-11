#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    int amounts[11]; 
    
    amounts[1] = 100; 
    amounts[2] = 500; 
    amounts[3] = 1000; 
    amounts[4] = 5000; 
    amounts[5] = 10000; 
    amounts[6] = 25000; 
    amounts[7] = 50000; 
    amounts[8] = 100000; 
    amounts[9] = 500000; 
    amounts[10] = 1000000; 

    int sum = 1691600;

    int n; cin >> n; 

    for (int x = 0; x < n; x++) {
        int a; cin >> a;
        sum -= amounts[a];
    }

    int a; cin >> a; 

    if (a > sum/(10-n)) cout << "deal";
    else cout << "no deal";

}