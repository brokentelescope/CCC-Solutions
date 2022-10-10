#include <string>
#include <iostream> 
using namespace std;

int main() {
    int n;
    cin >> n;

    int max = 0;

    string bidder;
    for (int x = 0; x < n; x ++) {
        int bid; 
        string name;
        cin >> name;
        cin >> bid;

        if (bid > max) {
            max = bid;
            bidder = name;
        }
    }

    cout << bidder;
}