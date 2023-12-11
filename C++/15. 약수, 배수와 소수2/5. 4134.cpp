#include <iostream>
#include <cmath>

using namespace std;

bool prime(long long n) {
    if (n == 0 || n == 1)
        return false;
    if (n == 2 || n == 3)
        return true;

    for (int i = 2; i < sqrt(n) + 1; i++)
        if (n % i == 0)
            return false;

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long t, a;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> a;

        while (!prime(a))
            a++;

        cout << a << '\n';
    }

    return 0;
}