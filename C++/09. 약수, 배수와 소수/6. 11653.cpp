#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int m = 2; m <= sqrt(n); m++) {
        while (n % m == 0) {
            cout << m << endl;
            n /= m;
        }
    }

    if (n != 1)
        cout << n << endl;

    return 0;
}