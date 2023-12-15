#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, a, max = 0, min = 1000000;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a > max)
            max = a;
        if (a < min)
            min = a;
    }

    cout << max * min;

    return 0;
}