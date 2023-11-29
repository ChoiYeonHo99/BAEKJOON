#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int m, n, sum = 0, min = 10000;
    bool prime;

    cin >> m;
    cin >> n;

    for (int i = m; i < n+1; i++) {
        if (i == 1)
            continue;

        prime = true;
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                prime = false;
                break;
            }
        }

        if (prime) {
            sum += i;
            if (i < min)
                min = i;
        }
    }

    if (sum == 0)
        cout << -1 << endl;
    else {
        cout << sum << endl;
        cout << min << endl;
    }

    return 0;
}