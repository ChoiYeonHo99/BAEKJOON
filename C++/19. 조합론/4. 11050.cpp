#include <iostream>

using namespace std;

int factorial(int n) {
    int result = 1;

    for (int i = 2; i < n + 1; i++)
        result *= i;

    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    if (n == k)
        cout << 1;
    else
        cout << factorial(n) / (factorial(k) * factorial(n - k));

    return 0;
}