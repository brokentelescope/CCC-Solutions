#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    string a, b;

    getline(cin, a); getline(cin, b); 

    a.erase(remove(a.begin(), a.end(), ' '), a.end());
    b.erase(remove(b.begin(), b.end(), ' '), b.end());

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    if (a == b) cout << "Is an anagram.";
    else cout << "Is not an anagram.";
}