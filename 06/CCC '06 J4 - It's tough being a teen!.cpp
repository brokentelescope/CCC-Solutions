#include <bits/stdc++.h>

using namespace std;

vector<int> graph[8];
int indeg[8]; 

void topsort() {
    vector<int> q;
    int cnt = 0; 
    int order[8];

    for (int x = 1; x <= 7; x++) {
        if (indeg[x] == 0) q.push_back(x);
    }

    while (!q.empty()) {
        sort(q.begin(), q.end(), greater<int>());
        int v = q.back();
        q.pop_back();
        cnt ++;
        order[cnt] = v; 

        for (int x: graph[v]) {
            indeg[x] --;
            if (indeg[x] == 0) {
                q.push_back(x);
            } 
        }
    }
    if (cnt != 7) {
        cout << "Cannot complete these tasks. Going to bed.";
    }
    else {
        for (int x = 1; x <= 7; x++) cout << order[x] << " ";
    }
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    indeg[1] = 1; 
    indeg[2] = 0;
    indeg[3] = 0; 
    indeg[4] = 2; 
    indeg[5] = 1;
    indeg[6] = 0; 
    indeg[7] = 1; 

    graph[1] = {4, 7};
    graph[2] = {1};
    graph[3] = {4, 5};

    while (true) {
        int a, b;
        cin >> a >> b;
        if (a == 0 && b == 0) break; 

        graph[a].push_back(b);
        indeg[b] ++;
    }

    topsort();
}