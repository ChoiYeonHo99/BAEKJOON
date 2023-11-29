#include <iostream>

using namespace std;

int main() {
    int a, b, v, day = 0, current = 0;
    cin >> a >> b >> v;
    int h = a - b;

    if (a >= v)
        day = 1;
    else
        if ((v - a) % h > 0)
            day = (v - a) / h + 2;
        else
            day = (v - a) / h + 1;

    cout << day << endl;

    return 0;
}