#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    bool VPS;
    string input;
    stack<int> myStack;
    for (int i = 0; i < t; i++) {
        while(!myStack.empty())
            myStack.pop();

        cin >> input;
        VPS = true;

        for (int j = 0; j < input.size(); j++) {
            if (input[j] == '(')
                myStack.push(1);
            else {
                if (myStack.empty()) {
                    VPS = false;
                    break;
                }
                else
                    myStack.pop();
            }
        }

        if (!myStack.empty())
            VPS = false;

        if (VPS)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    
    return 0;
}