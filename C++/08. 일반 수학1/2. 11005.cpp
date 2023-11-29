#include <iostream>

using namespace std;

int main() {
    int n, b;
    string result = "";
  
    cin >> n >> b;

    while (n > 0) {
        int value = n % b;
        if (value <= 9) {
            result = to_string(value) + result;
        }
        else {
            char digit = 'A' + value - 10;
            result = digit + result;
        }
        n /= b;
    }

    cout << result << endl;

    return 0;
}