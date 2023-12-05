#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, a, count = 0;
    cin >> n >> m;

    map<int, int> dictionary;
    for (int i = 0; i < n; i++) {
        cin >> a;
        dictionary[a] = 1;
    }

    for (int i = 0; i < m; i++) {
        cin >> a;
        if (dictionary.find(a) != dictionary.end())
            count++;
    }

    cout << n + m - 2 * count;

    return 0;
}