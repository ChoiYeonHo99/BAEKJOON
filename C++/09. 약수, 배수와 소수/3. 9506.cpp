#include <iostream>

using namespace std;

int main() {
    int n, sum = 0, index = 0, arr[100000];

    while (1) {
        cin >> n;
        if (n == -1)
            return 0;

        sum = 0, index = 0;

        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sum += i;
                arr[index] = i;
                index++;
            }
        }

        if (sum == n) {
            cout << n << " = ";
            for (int i = 0; i < index - 1; i++) {
                cout << arr[i] << " + ";
            }
            cout << arr[index - 1] << endl;
        }
        else
            cout << n << " is NOT perfect." << endl;
    }

    return 0;
}