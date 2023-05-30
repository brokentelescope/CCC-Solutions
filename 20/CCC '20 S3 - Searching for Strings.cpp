// this question is so hard god damnbro 
// rolling hash algorithm
// have to optimize calculating powers or else it will TLE

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll mod = 10000000631;
const ll b = 31;

ll dp[200000];

set<ll> vis;
int n, m, freqa[300], freqb[300];

bool comp() {
    for (int x = 'a'; x <= 'z'; x++) {
        if (freqa[x] != freqb[x]) return false;
    }
    return true;
}


ll power(int base, int exp) {
    return dp[exp];
}

ll hash_(string word) {

    int n = word.length();

    ll ans = 0;

    for (int x = 0; x < word.length(); x++) {
        ans = (ans + power(b, n-x-1) * ((int)word[x]-(int)'a'+1)) % mod;
    }

    return ans;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    string big, small;

    cin >> small >> big;

    int n = small.length(), m = big.length();

    dp[0] = 1;

    for (int x = 1; x < 200000; x++) {
        dp[x] = (dp[x-1] * b) % mod;
    }

    for (int x = 'a'; x <= 'z'; x++) {freqa[x] = 0; freqb[x] = 0;}

    for (int x = 0; x < n; x++) {
        freqa[small[x]] ++;
        freqb[big[x]] ++;
    }
    // calculate first hash 
    ll hash = hash_(big.substr(0, n));

    int ans = 0;

    if (comp()) {
        ans ++;
        vis.insert(hash);
    }

    for (int x = 1; x+n-1 < m; x++) {
        freqb[big[x-1]] --;
        freqb[big[x+n-1]] ++;
        // rolling hash
        hash = (hash - power(b, n-1) * ((int)big[x-1]-(int)'a'+1)) % mod;
        if (hash < 0) hash += mod;

        hash = (hash * b) % mod;
        hash = (hash + (int)big[x+n-1]-(int)'a'+1) % mod;

        if (comp() && vis.count(hash) == 0) {
            ans ++;
            vis.insert(hash);
        }

        // cout << big.substr(x, n) << " roll hash: " << hash << " real hash: " << hash_(big.substr(x, n)) << "\n" ;

    }

    cout << ans;
}
