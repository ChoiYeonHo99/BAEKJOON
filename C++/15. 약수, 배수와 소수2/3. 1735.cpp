#include <iostream>

using namespace std;

int gcd(int n1, int n2) {
    if (n1 < n2) {
        int temp = n2;
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

    int a1, a2, b1, b2, n1, n2, temp;

    cin >> a1 >> a2;
    cin >> b1 >> b2;

    temp = gcd(a2, b2);
    n2 = a2 / temp * b2;
    n1 = a1 * (n2 / a2) + b1 * (n2 / b2);

    temp = gcd(n1, n2);
    while (temp != 1) {
        n1 /= temp;
        n2 /= temp;
        temp = gcd(n1, n2);
    }

    cout << n1 << ' ' << n2;

    return 0;
}