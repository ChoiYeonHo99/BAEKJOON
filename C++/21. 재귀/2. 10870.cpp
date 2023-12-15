#include <iostream>

using namespace std;

int finonacci(int n) {
    if (n == 0)
        return 0;

    if (n == 1 || n == 2)
        return 1;

    return finonacci(n - 1) + finonacci(n - 2);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    cout << finonacci(n);

    return 0;
}