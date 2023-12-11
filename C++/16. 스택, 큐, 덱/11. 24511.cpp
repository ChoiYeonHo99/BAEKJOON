#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n;

    int structure[n];
    for (int i = 0; i < n; i++)
        cin >> structure[i];

    deque<int> myDeque;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if (structure[i] == 0)
            myDeque.push_back(x);
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> x;
        myDeque.push_front(x);
        cout << myDeque.back() << ' ';
        myDeque.pop_back();
    }

    return 0;
}