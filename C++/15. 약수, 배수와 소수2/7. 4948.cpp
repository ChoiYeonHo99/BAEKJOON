#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int prime[250000] = {0};
    for (int i = 2; i < 250000; i++) {
        if (prime[i] == 1)
            continue;

        for (int j = i + i; j < 250000; j += i)
            prime[j] = 1;
    }

    int n, count;
    while (1) {
        cin >> n;
        if (n == 0)
            break;

        count = 0;
        for (int i = n + 1; i < 2 * n + 1; i++)
            if (i >= 2 && prime[i] == 0)
                count++;

        cout << count << '\n';
    }

    return 0;
}