#include <iostream>

using namespace std;

int gcd(int n1, int n2) {
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

    int n, g, result = 0;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    g = arr[1] - arr[0];
    for (int i = 1; i < n-1; i++)
        g = gcd(g, arr[i + 1] - arr[i]);

    for (int i = 0; i < n-1; i++)
        result += (arr[i + 1] - arr[i]) / g - 1;

    cout << result;

    return 0;
}