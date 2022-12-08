#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    unordered_map<char, int> presses;
    unordered_map<char, int> num; 

    int cnt = 1; 
    int cnt2 = 2;
    for (int x = 97; x <= 122; x++) {
        if (cnt == 4) cnt = 1;
        presses[char(x)] = cnt; cnt ++;
    }

    presses['s'] = 4;
    presses['t'] = 1;
    presses['u'] = 2;
    presses['v'] = 3;
    presses['w'] = 1;
    presses['x'] = 2;
    presses['y'] = 3;
    presses['z'] = 4;

    num['a'] = 2;
    num['b'] = 2;
    num['c'] = 2;
    num['d'] = 3;
    num['e'] = 3;
    num['f'] = 3;
    num['g'] = 4;
    num['h'] = 4;
    num['i'] = 4;
    num['j'] = 5;
    num['k'] = 5;
    num['l'] = 5;
    num['m'] = 6;
    num['n'] = 6;
    num['o'] = 6;
    num['p'] = 7;
    num['q'] = 7;
    num['r'] = 7;
    num['s'] = 7;
    num['t'] = 8;
    num['u'] = 8;
    num['v'] = 8;
    num['w'] = 9;
    num['x'] = 9;
    num['y'] = 9;
    num['z'] = 9;

    while (true) {
        string a; cin >> a;
        if (a == "halt") break; 

        int last = 0; 

        int sum = 0;
        for (int x = 0; x < a.length(); x++) {
            if (num[a[x]] == last) sum += 2;
            sum += presses[a[x]];
            last = num[a[x]];
        }

        cout << sum << endl;
    }
}