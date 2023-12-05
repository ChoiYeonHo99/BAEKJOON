#include <iostream>

using namespace std;

int main() {
    int n, kg5, kg3, total;
    cin >> n;

    kg5 = n / 5;
    kg3 = (n - kg5 * 5) / 3;
    total = kg5 * 5 + kg3 * 3;
    while (total != n && kg5 >= 0) {
        kg5--;
        kg3 = (n - kg5 * 5) / 3;
        total = kg5 * 5 + kg3 * 3;
    }

    if (kg5 < 0)
        cout << -1 << endl;
    else
        cout << kg5 + kg3 << endl;
    
    return 0;
}