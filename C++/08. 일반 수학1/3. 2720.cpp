#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int C, Q = 25, D = 10, N = 5, P = 1;
        int q, d, n, p;
        cin >> C;

        q = C / Q;
        C %= Q;

        d = C / D;
        C %= D;

        n = C / N;
        C %= N;

        p = C / P;
        C %= P;

        cout << q << " " << d << " " << n << " " << p << endl;
    }

    return 0;
}