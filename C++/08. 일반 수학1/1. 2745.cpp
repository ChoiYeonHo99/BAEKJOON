#include <iostream>
#include <cmath>

using namespace std;

int main() {
    string n;
    int b, result = 0;
  
    cin >> n >> b;

    for (int i = 0; i < n.length(); i++) {
        char digit = n[i];
        int value = 0;

        if (digit >= '0' && digit <= '9') {
            value = digit - '0';
        } else if (digit >= 'A' && digit <= 'Z') {
            value = digit - 'A' + 10;
        }

        result += value * pow(b, n.length() - i - 1);
    }

    cout << result << endl;

    return 0;
}