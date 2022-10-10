#include <iostream>
using namespace std;

int main() {
    int n; 
    cin >> n;

    int cnt = 0; 

    for (int x = 0; x < n; x++) {
        int points, fouls; 

        cin >> points;
        cin >> fouls; 

        int rating = points*5 - fouls*3;

        if (rating > 40) {
            cnt ++;
        }
    }

    cout << cnt; 

    if (cnt == n) {
        cout << "+";
    }

}