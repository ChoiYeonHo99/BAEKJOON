#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, command, x;
    cin >> n;

    stack<int> myStack;
    for (int i = 0; i < n; i++) {
        cin >> command;

        if (command == 1) {
            cin >> x;
            myStack.push(x);
        }
        if (command == 2) {
            if (myStack.empty())
                cout << -1 << '\n';
            else {
                cout << myStack.top() << '\n';
                myStack.pop();
            }
        }
        if (command == 3)
            cout << myStack.size() << '\n';
        if (command == 4) {
            if (myStack.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
        if (command == 5) {
            if (myStack.empty())
                cout << -1 << '\n';
            else
                cout << myStack.top() << '\n';
        }
    }
    
    return 0;
}