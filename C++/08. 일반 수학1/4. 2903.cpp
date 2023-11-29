#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n, result = 1;
    cin >> n;

    for (int i = 0; i < n; i++) {
        result *= 4;
    }
    result = pow(sqrt(result) + 1, 2);

    cout << result << endl;

    return 0;
}