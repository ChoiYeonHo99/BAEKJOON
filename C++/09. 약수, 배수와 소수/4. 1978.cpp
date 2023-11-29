#include <iostream>

using namespace std;

int main() {
    int n, num, arr[100], count = 0;
    bool prime;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num;
        arr[i] = num;
    }

    for (int i = 0; i < n; i++) {
        prime = true;
        if (arr[i] == 1)
            continue;

        for (int j = 2; j < arr[i]; j++)
            if (arr[i] % j == 0) {
                prime = false;
                break;
            }

        if (prime)
            count++;
    }

    cout << count << endl;

    return 0;
}