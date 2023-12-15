#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, result = 1;
    cin >> n;

    for (int i = 2; i < n + 1; i++)
        result *= i;

    cout << result;

    return 0;
}