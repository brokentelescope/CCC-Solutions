#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    
    cout << fixed; cout << setprecision(2);

    int d, e , w; cin >> d >> e >> w;

    float one = max(0, d-100)*.25 + e*.15 + w*.20;
    float two = max(0, d-250)*.45 + e*.35 + w*.25; 

    cout << "Plan A costs " << one << endl; 
    cout << "Plan B costs " << two << endl;

    if (one < two) cout << "Plan A is cheapest.";
    else if (one > two) cout << "Plan B is cheapest.";
    else cout << "Plan A and B are the same price.";

}