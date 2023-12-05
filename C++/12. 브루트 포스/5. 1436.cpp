#include <iostream>

using namespace std;

int main() {
    int n, count = 0, num = 666;
    cin >> n;

    while (count <= 10000) {
        int temp = num;
        while (temp > 100) {
            if (temp % 1000 == 666) {
                count++;
                break;
            }

            temp /= 10;
        }

        if (count == n) {
            cout << num << endl;
            return 0;
        }

        num++;
    }
    
    return 0;
}