#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i < n; i++) {
        int num = i, sum = 0;

        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }

        if (sum + i == n) {
            cout << i << endl;
            return 0;
        }
    }

    cout << 0 << endl;
    return 0;
}