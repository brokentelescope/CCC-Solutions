#include <bits/stdc++.h>

using namespace std;

const int mm = 1e6+6;

string s;

int n, psaA[mm], psaB[mm], psaC[mm], numA, numB, numC, ans = 1e9;

char arr[2*mm];

void f(int a[], int b[], int na, int nb, int idx) {
    int notAinA = na - (a[idx+na-1] - a[idx-1]);
    int notBinB = nb - (b[idx+na+nb-1] - b[idx+na-1]);
    int BinA = b[idx+na-1] - b[idx-1];
    int AinB = a[idx+na+nb-1] - a[idx+na-1];

    ans = min(ans, notAinA + notBinB - min(BinA, AinB));
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    cin >> s;

    n = s.length();

    psaA[0] = psaB[0] = psaC[0] = 0;

    for (int x = 1; x <= n; x++) {
        arr[x] = s[x-1];
        psaA[x] = psaA[x-1] + (arr[x] == 'A');
        psaB[x] = psaB[x-1] + (arr[x] == 'B');
        psaC[x] = psaC[x-1] + (arr[x] == 'C');
    }

    numA = psaA[n];
    numB = psaB[n];
    numC = psaC[n];

    for (int x = 1; x <= n; x++) {
        if (x+numA+numB-1 <= n) {
            f(psaA, psaB, numA, numB, x);
            f(psaB, psaA, numB, numA, x);
        }
        if (x+numA+numC-1 <= n) {
            f(psaA, psaC, numA, numC, x);
            f(psaC, psaA, numC, numA, x);
        } 
        if (x+numB+numC-1 <= n) {
            f(psaB, psaC, numB, numC, x);
            f(psaC, psaB, numC, numB, x);
        } 
    }

    cout << ans << "\n";
}