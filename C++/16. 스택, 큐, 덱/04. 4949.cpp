#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    bool VPS;
    string input;
    stack<int> myStack;
    while (1) {
        while(!myStack.empty())
            myStack.pop();

        getline(cin, input);
        if (input[0] == '.')
            return 0;

        VPS = true;
        for (int j = 0; j < input.size(); j++) {
            if (input[j] == '(')
                myStack.push(1);
            else if (input[j] == ')') {
                if (myStack.empty()) {
                    VPS = false;
                    break;
                }
                else {
                    if (myStack.top() == 1)
                        myStack.pop();
                    else {
                        VPS = false;
                        break;
                    }
                }
            }

            else if (input[j] == '[')
                myStack.push(2);
            else if (input[j] == ']') {
                if (myStack.empty()) {
                    VPS = false;
                    break;
                }
                else {
                    if (myStack.top() == 2)
                        myStack.pop();
                    else {
                        VPS = false;
                        break;
                    }
                }
            }
        }

        if (!myStack.empty())
            VPS = false;

        if (VPS)
            cout << "yes\n";
        else
            cout << "no\n";
    }
    
    return 0;
}