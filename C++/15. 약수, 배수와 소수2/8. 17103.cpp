#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int prime[1000000] = {0};
    prime[0] = 1;
    prime[1] = 1;
    for (int i = 2; i < 1000000; i++) {
        if (prime[i] == 1)
            continue;

        for (int j = i + i; j < 1000000; j += i)
            prime[j] = 1;
    }

    int t, n, count;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        count = 0;

        for (int i = 2; i <= n / 2; i++)
            if (prime[i] == 0 && prime[n - i] == 0)
                count++;

        cout << count << '\n';
    }

    return 0;
}