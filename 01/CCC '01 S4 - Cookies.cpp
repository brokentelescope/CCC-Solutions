#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

float obtuse(float a, float b, float c) {
    if (a*a + b*b < c*c) {
        return c;
    }
    
    if (b*b + c*c < a*a) {
        return a;
    }
    
    if (c*c + a*a < b*b) {
        return b;
    }
    
    return -1;
}

float heron(float ax, float bx, float cx, float ay, float by, float cy) {
    
    float a = sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by));
    float b = sqrt((bx-cx)*(bx-cx) + (by-cy)*(by-cy));
    float c = sqrt((cx-ax)*(cx-ax) + (cy-ay)*(cy-ay));
    
    // cout << a << " " << b << " " << c;
    // cout << endl;
    if (obtuse(a,b,c) != -1) {
        return obtuse(a,b,c);
    }
    
    float s = (a+b+c)/2; 
    
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    if (area == 0) {
        return 0;
    } 

    float radius = (a*b*c)/(4*area);
    
    return radius*2;

}

int main()
{
    cout << fixed;
    cout << setprecision(2);
    int n; 
    cin >> n;
    
    int chips[n][2];
    
    for (int x = 0; x < n; x++) {
        cin >> chips[x][0];
        cin >> chips[x][1];
    }
    
    float ans = 0;
    for (int x = 0; x < n; x++) {
        for (int y = 1; y < n; y++) {
            for (int z = 2; z < n; z++) {
                if (heron(chips[x][0], chips[y][0], chips[z][0], chips[x][1], chips[y][1], chips[z][1]) > ans) {
                    ans = heron(chips[x][0], chips[y][0], chips[z][0], chips[x][1], chips[y][1], chips[z][1]);
                }
            }
        }
    } 
    cout << ans;
}
