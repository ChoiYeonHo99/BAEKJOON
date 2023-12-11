#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k, x, size, sum = 0;
    cin >> k;

    stack<int> myStack;
    for (int i = 0; i < k; i++) {
        cin >> x;

        if (x == 0)
            myStack.pop();
        else
            myStack.push(x);
    }

    size = myStack.size();
    for (int i = 0; i < size; i++) {
        sum += myStack.top();
        myStack.pop();
    }

    cout << sum;
    
    return 0;
}