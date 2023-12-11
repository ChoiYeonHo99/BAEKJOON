#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, a;
    cin >> n;

    queue<int> myQueue;
    string command;
    for (int i = 0; i < n; i++) {
        cin >> command;
        if (command == "push") {
            cin >> a;
            myQueue.push(a);
        }
        else if (command == "pop") {
            if (myQueue.size() == 0)
                cout << -1 << '\n';
            else {
                cout << myQueue.front() << '\n';
                myQueue.pop();
            }
        }
        else if (command == "size")
            cout << myQueue.size() << '\n';
        else if (command == "empty") {
            if (myQueue.size() == 0)
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
        else if (command == "front") {
            if (myQueue.size() == 0)
                cout << -1 << '\n';
            else
                cout << myQueue.front() << '\n';
        }
        else if (command == "back") {
            if (myQueue.size() == 0)
                cout << -1 << '\n';
            else
                cout << myQueue.back() << '\n';
        }
    }
    
    return 0;
}