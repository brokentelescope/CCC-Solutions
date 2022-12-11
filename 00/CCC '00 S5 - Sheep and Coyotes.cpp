//passes all ccc cases, doesn't pass dmoj case 6
//the decimal precision isn't enough 
//maybe try making the positions integers by multiplying by 100 

#include <bits/stdc++.h>

using namespace std;

pair<double, double> sheep[1000];

int n;

long double distance(double x1, double x2, double y2) {
    return (x2-x1)*(x2-x1) + y2*y2;
}

int closest(double coyote) {
    long double dist = numeric_limits<long double>::max(); 
    int i = -1;
    for (int x = 0; x < n; x++) {
        long double d = distance(coyote, sheep[x].first, sheep[x].second);
        if (d < dist) {
            dist = d; 
            i = x;
        }
    }    
    return i;
}

int main() {
    cout << fixed; cout << setprecision(2); 

    cin.sync_with_stdio(0); cin.tie(0); 

    cin >> n; 

    for (int x = 0; x < n; x++) cin >> sheep[x].first >> sheep[x].second;
    
    set<int> s; 

    for (double x = 0.0; x <= 1000.0; x += 0.01) {
        int close = closest(x);
        if (s.count(close) == 0) {
            s.insert(close);
            cout << "The sheep at (" << sheep[close].first << ", " << sheep[close].second << ") might be eaten." << endl;
        }
    }
}
