#include <iostream>

using namespace std;

int main() {
    int n, a, arr[10] = {0};
    cin >> n;

    while (n > 0) {
        a = n % 10;
        arr[a]++;
        n /= 10;
    }

    for (int i = 9; i >= 0; i--)
        for (int j = 0; j < arr[i]; j++)
            cout << i;
    
    return 0;
}