#include <iostream>

using namespace std;

int main() {
    int n, k, index = 0;
    cin >> n >> k;
    int arr[n];

    for (int i = 1; i < n + 1; i++) {
        if (n % i == 0) {
            arr[index] = i;
            index++;
        }
    }

    if (k > index)
        cout << 0 << endl;
    else
        cout << arr[k-1] << endl;

    return 0;
}