#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> my_list(n, 0);
    for (int i = 0; i < n; ++i) {
        cin >> my_list[i];
    }
    
    vector<int> d(n, 0);
    d[0] = 1;
    
    for (int i = 0; i < n-1; ++i) {
        if (d[i] == 1) {
            for (int j = i+1; j < n; ++j) {
                if (d[j] == 0 && (j-i)*(1+abs(my_list[i]-my_list[j])) <= k) {
                    d[j] = 1;
                }
            }
        }
    }
    
    if (d[n-1] == 1) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    
    return 0;
}