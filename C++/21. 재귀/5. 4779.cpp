#include <iostream>
#include <cmath>

using namespace std;

void solution(int n) {
    if (n == 0) {
        cout << '-';
        return;
    }

    int size = pow(3, n - 1);

    solution(n - 1);
    for (int i = 0; i < size; ++i)
        cout << ' ';
    solution(n - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    while (cin >> n) {
        solution(n);
        cout << '\n';
    }

    return 0;
}