#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    string line;
    
    getline(cin, line);

    reverse(line.begin(), line.end()); 

    unordered_map<char, int> key; 

    key['I'] = 1; 
    key['V'] = 5; 
    key['X'] = 10; 
    key['L'] = 50; 
    key['C'] = 100; 
    key['D'] = 500; 
    key['M'] = 1000; 

    unordered_map<char, int> key2; 

    key2['1'] = 1;
    key2['2'] = 2;
    key2['3'] = 3;
    key2['4'] = 4;
    key2['5'] = 5;
    key2['6'] = 6;
    key2['7'] = 7;
    key2['8'] = 8;
    key2['9'] = 9;
    key2['0'] = 0;

    int sum = 0; 
    char last = 'I';

    for (int x = 0; x < line.length(); x = x + 2) {
        int next = key[line[x]] * key2[line[x+1]];
        if (key[line[x]] < key[last]) {
            sum -= next;
        }
        else {
          sum += next;  
        }
        last = line[x];
    }
    cout << sum;
}