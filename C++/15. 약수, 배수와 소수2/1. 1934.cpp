#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t, a, b, n, x;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> a >> b;
        x = 2;
        n = 1;
        while (a > 1) {
            if (a % x == 0) {
                if (b % x == 0)
                    b /= x;
                a /= x;
                n *= x;
            }
            else
                x++;
        }
        n *= b;

        cout << n << '\n';
    }

    return 0;
}