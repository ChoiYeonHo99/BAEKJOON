#include <iostream>

using namespace std;

int gcd(long long n1, long long n2) {
    if (n1 < n2) {
        long long temp = n2;
        n2 = n1;
        n1 = temp;
    }

    if (n1 == n2)
        return n1;

    int a = 1;
    while (a != 0) {
        a = n1 % n2;
        if (a == 0)
            return n2;

        n1 = n2;
        n2 = a;
    }

    return n2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long a, b, g, n;

    cin >> a >> b;
    g = gcd(a, b);
    n = a / g * b;

    cout << n;

    return 0;
}