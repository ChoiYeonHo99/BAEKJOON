#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    stack<int> myStack1;
    stack<int> myStack2;

    bool possible = true;
    int n, a, next = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        myStack2.push(a);
    }
    for (int i = 0; i < n; i++) {
        a = myStack2.top();
        myStack2.pop();
        myStack1.push(a);
    }

    while(1) {
        if (next > n)
            break;

        if (!myStack2.empty() && myStack2.top() == next) {
            myStack2.pop();
            next++;
            continue;
        }

        if (!myStack1.empty()) {
            if (myStack1.top() == next) {
                myStack1.pop();
                next++;
                continue;
            }
            else {
                a = myStack1.top();
                myStack1.pop();
                myStack2.push(a);
            }
        }
        else {
            possible = false;
            break;
        }
    }

    if (possible)
        cout << "Nice";
    else
        cout << "Sad";
    
    return 0;
}