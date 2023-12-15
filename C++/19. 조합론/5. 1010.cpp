#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t, n, m, r;
    long long result = 1;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n >> m;
        result = 1;
        r = 1;

        for (int j = m; j > m - n; j--) {
            result *= j;
            result /= r;
            r++;
        }

        cout << result << '\n';
    }

    return 0;
}