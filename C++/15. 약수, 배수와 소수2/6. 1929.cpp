#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    
    int prime[1000001] = {0};
    for (int i = 2; i < m + 1; i++) {
        if (prime[i] == 1)
            continue;

        for (int j = i + i; j < m + 1; j += i)
            prime[j] = 1;
    }

    for (int i = n; i < m + 1; i++)
        if (i >= 2 && prime[i] == 0)
            cout << i << '\n';

    return 0;
}