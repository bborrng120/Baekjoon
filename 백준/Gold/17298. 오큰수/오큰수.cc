#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int answer[1000001];
int my_list[1000001];
vector<int> temp;

int main()
{
    int n;
    cin >> n;
    
    memset(answer, -1, sizeof(answer));
    
    for (int i = 0; i < n; ++i) {
        cin >> my_list[i];
    }
    
    temp.push_back(0);
    for (int i = 1; i < n; ++i) {
        while (!temp.empty() && my_list[i] > my_list[temp.back()]) {
            answer[temp.back()] = my_list[i];
            temp.pop_back();
        }
        temp.push_back(i);
    }
    
    for (int i = 0; i < n; ++i) {
        cout << answer[i] << " ";
    }
}