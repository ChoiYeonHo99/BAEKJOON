#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, num, direction;
    cin >> n;

    int move[n];
    for (int i = 1; i < n + 1; i++)
        cin >> move[i];
    
    deque<int> myDeque;
    for (int i = 1; i < n + 1; i++)
        myDeque.push_back(i);

    while (!myDeque.empty()) {
        num = myDeque.front();
        myDeque.pop_front();
        cout << num << ' ';

        direction = move[num];
        if (direction > 0) {
            for (int i = 0; i < direction - 1; i++) {
                myDeque.push_back(myDeque.front());
                myDeque.pop_front();
            }
        }
        else {
            for (int i = 0; i < -1 * direction; i++) {
                myDeque.push_front(myDeque.back());
                myDeque.pop_back();
            }
        }
    }
    
    return 0;
}