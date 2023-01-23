#include <bits/stdc++.h>

using namespace std;

int main()
{
    int c, r, x, y;
    int movex, movey;
    
    cin >> c >> r;
    
    x = 0;
    y = 0;
    
    while (true) {
        cin >> movex >> movey;
        
        if (movex == 0 && movey == 0) {
            break;
        }
        
        if (movex < 0) {
            x = max(0, x+movex);
        }
        
        else if (movex > 0) {
            x = min(c, x+movex);
        }
        
        if (movey < 0) {
            y = max(0, y+movey);
        }
        
        else if (movey > 0) {
            y = min(r, y+movey);
        }
        
        cout << x << " " << y << endl;
    }
    return 0;
}
