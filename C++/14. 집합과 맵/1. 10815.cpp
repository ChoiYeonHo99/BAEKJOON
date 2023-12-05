#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, a;
    cin >> n;

    map<int, bool> myMap;
    for (int i = 0; i < n; i++) {
        cin >> a;
        myMap.insert({a, true});
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> a;
        if (myMap.find(a) != myMap.end())
            cout << 1 << ' ';
        else
            cout << 0 << ' ';
    }

    return 0;
}