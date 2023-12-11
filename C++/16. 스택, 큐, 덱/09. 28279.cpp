#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, command, a;
    cin >> n;
    
    deque<int> myDeque;
    for (int i = 0; i < n; i++) {
        cin >> command;
        if (command == 1) {
            cin >> a;
            myDeque.push_front(a);
        }
        else if (command == 2) {
            cin >> a;
            myDeque.push_back(a);
        }
        else if (command == 3) {
            if (myDeque.empty())
                cout << -1 << '\n';
            else {
                cout << myDeque.front() << '\n';
                myDeque.pop_front();
            }
        }
        else if (command == 4) {
            if (myDeque.empty())
                cout << -1 << '\n';
            else {
                cout << myDeque.back() << '\n';
                myDeque.pop_back();
            }
        }
        else if (command == 5)
            cout << myDeque.size() << '\n';
        else if (command == 6) {
            if (myDeque.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
        else if (command == 7) {
            if (myDeque.empty())
                cout << -1 << '\n';
            else
                cout << myDeque.front() << '\n';
        }
        else if (command == 8) {
            if (myDeque.empty())
                cout << -1 << '\n';
            else
                cout << myDeque.back() << '\n';
        }
    }
    
    return 0;
}