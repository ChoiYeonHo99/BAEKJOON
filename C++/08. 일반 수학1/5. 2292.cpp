#include <iostream>

using namespace std;

int main() {
    int n, count = 1, distance = 1;
    cin >> n;

    while (n > 1) {
        n -= count * 6;
        count++;
        distance++;
    }

    cout << distance << endl;

    return 0;
}