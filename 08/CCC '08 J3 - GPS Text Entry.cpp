#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    string a; 
    getline(cin, a); 

    a = a + '*';

    a = 'A' + a;

    unordered_map<char, pair<int, int>> key;

    key['A'] = {0, 0}; 
    key['B'] = {0, 1}; 
    key['C'] = {0, 2}; 
    key['D'] = {0, 3}; 
    key['E'] = {0, 4}; 
    key['F'] = {0, 5}; 

    key['G'] = {1, 0}; 
    key['H'] = {1, 1}; 
    key['I'] = {1, 2}; 
    key['J'] = {1, 3}; 
    key['K'] = {1, 4}; 
    key['L'] = {1, 5}; 

    key['M'] = {2, 0}; 
    key['N'] = {2, 1}; 
    key['O'] = {2, 2}; 
    key['P'] = {2, 3}; 
    key['Q'] = {2, 4}; 
    key['R'] = {2, 5}; 

    key['S'] = {3, 0}; 
    key['T'] = {3, 1}; 
    key['U'] = {3, 2}; 
    key['V'] = {3, 3}; 
    key['W'] = {3, 4}; 
    key['X'] = {3, 5}; 

    key['Y'] = {4, 0}; 
    key['Z'] = {4, 1}; 
    key[' '] = {4, 2}; 
    key['-'] = {4, 3}; 
    key['.'] = {4, 4}; 
    key['*'] = {4, 5};

    int cnt = 0; 
    for (int x = 1; x < a.length(); x++) {
        cnt += abs(key[a[x]].first - key[a[x-1]].first);
        cnt += abs(key[a[x]].second - key[a[x-1]].second);
    }    
    cout << cnt;
}