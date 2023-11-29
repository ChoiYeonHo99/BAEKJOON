#include <iostream>

using namespace std;

int main() {
    int x, n = 1;
    cin >> x;

    while (x > n) {
        x -= n;
        n++;
    }

    if (n % 2 == 0)
        cout << x << "/" << n+1-x << endl;
    else
        cout << n+1-x << "/" << x << endl;

    return 0;
}