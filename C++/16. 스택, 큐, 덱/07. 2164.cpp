#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    deque<int> myDeque;
    for (int i = 1; i < n + 1; i++)
        myDeque.push_back(i);

    while (myDeque.size() > 1) {
        myDeque.pop_front();
        myDeque.push_back(myDeque.front());
        myDeque.pop_front();
    }

    cout << myDeque.front();
    
    return 0;
}