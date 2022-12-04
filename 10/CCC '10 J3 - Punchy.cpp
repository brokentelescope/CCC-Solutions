#include <bits/stdc++.h>

using namespace std;

int nums[2];

void f1 (char x, int n) {nums[int(x)-65] = n;}
void f2 (char x) {cout<<nums[int(x)-65]<<endl;}
void f3 (char x, char y) {nums[int(x)-65] = nums[int(x)-65] + nums[int(y)-65];}
void f4 (char x, char y) {nums[int(x)-65] = nums[int(x)-65] * nums[int(y)-65];}
void f5 (char x, char y) {nums[int(x)-65] = nums[int(x)-65] - nums[int(y)-65];}
void f6 (char x, char y) {nums[int(x)-65] = nums[int(x)-65] / nums[int(y)-65];}

int main() {
    while (true) {
        int x; cin >> x;
        if(x==1) {
           char x; int n; cin >> x >> n; f1(x,n); 
        }
        if(x==2) {
           char x; cin >> x; f2(x); 
        }
        if(x==3) {
           char x, y; cin >> x >> y; f3(x, y); 
        }
        if(x==4) {
           char x, y; cin >> x >> y; f4(x, y); 
        }
        if(x==5) {
           char x, y; cin >> x >> y; f5(x, y); 
        }
        if(x==6) {
           char x, y; cin >> x >> y; f6(x, y); 
        }
        if(x==7) break;
    }
}