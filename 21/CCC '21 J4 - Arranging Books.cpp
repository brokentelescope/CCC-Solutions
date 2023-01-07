#include <bits/stdc++.h>

using namespace std;

const int inf = numeric_limits<int>::max();

int main() {
    cin.sync_with_stdio(0); cin.tie(0);    

    string line;

    getline(cin, line);

    int l = 0, m = 0, s = 0;

    for (int x = 0; x < line.length(); x++) {
        l += line[x] == 'L';
        m += line[x] == 'M';
        s += line[x] == 'S';
    }

    cout << l << " " << m << " " << s << endl;

    int l_dist[3] = {0, 0, 0};
    int m_dist[3] = {0, 0, 0};
    int s_dist[3] = {0, 0, 0};

    for (int x = 0; x < l; x++) {
        l_dist[0] += line[x] == 'L';
        m_dist[0] += line[x] == 'M';
        s_dist[0] += line[x] == 'S';
    }

    for (int x = l; x < l+m; x++) {
        l_dist[1] += line[x] == 'L';
        m_dist[1] += line[x] == 'M';
        s_dist[1] += line[x] == 'S';
    }

    for (int x = l+m; x < l+m+s; x++) {
        l_dist[2] += line[x] == 'L';
        m_dist[2] += line[x] == 'M';
        s_dist[2] += line[x] == 'S';
    }

    for (int x = 0; x < 3; x++) {
        cout << l_dist[x] << " ";
    }
    cout << endl;

    for (int x = 0; x < 3; x++) {
        cout << m_dist[x] << " ";
    }
    cout << endl;

    for (int x = 0; x < 3; x++) {
        cout << s_dist[x] << " ";
    }
    cout << endl;
    
    int swaps = 0;

    // swap any L's in M section with M's in L section 
    if (l_dist[1] != 0) {
        if (m_dist[0] != 0) {
            int temp = min(l_dist[1], m_dist[0]);
            swaps += temp;
            l_dist[1] -= temp;
            m_dist[0] -= temp;
        }
    }
    // swap any L's in S section with S's in L section 
    if (l_dist[2] != 0) {
        if (s_dist[0] != 0) {
            int temp = min(l_dist[2], s_dist[0]);
            swaps += temp;
            l_dist[2] -= temp;
            s_dist[0] -= temp;
        }
    }

    // if there are still L's in the M or S sections, we have to make a sub optimal swap
    if (l_dist[1] != 0) {
        int temp = min(l_dist[1], s_dist[0]);
        swaps += temp;
        l_dist[1] -= temp;
        s_dist[0] -= temp;
        s_dist[1] += temp;
    }

    if (l_dist[2] != 0) {
        int temp = min(l_dist[2], m_dist[0]);
        swaps += temp;
        l_dist[2] -= temp;
        m_dist[0] -= temp;
        m_dist[2] += temp;
    }

    // swap M's in S section with S's in M section 
    swaps += m_dist[2];

    cout << endl;
    for (int x = 0; x < 3; x++) {
        cout << l_dist[x] << " ";
    }
    cout << endl;

    for (int x = 0; x < 3; x++) {
        cout << m_dist[x] << " ";
    }
    cout << endl;

    for (int x = 0; x < 3; x++) {
        cout << s_dist[x] << " ";
    }
    cout << endl;

    cout << swaps;
}