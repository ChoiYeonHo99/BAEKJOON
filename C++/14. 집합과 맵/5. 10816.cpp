#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, a;
    cin >> n;

    map<int, int> dictionary;
    for (int i = 0; i < n; i++) {
        cin >> a;

        if (dictionary.find(a) != dictionary.end())
            dictionary[a]++;
        else
            dictionary[a] = 1;
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> a;

        if (dictionary.find(a) != dictionary.end())
            cout << dictionary[a] << ' ';
        else
            cout << 0 << ' ';
    }

    return 0;
}