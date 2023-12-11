#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    deque<int> myDeque;
    for (int i = 1; i < n + 1; i++)
        myDeque.push_back(i);

    cout << "<";
    while (1) {
        for (int i = 0; i < k - 1; i++) {
            myDeque.push_back(myDeque.front());
            myDeque.pop_front();
        }

        cout << myDeque.front();
        myDeque.pop_front();

        if (myDeque.size() > 0)
            cout << ", ";
        else
            break;
    }
    cout << ">";
    
    return 0;
}