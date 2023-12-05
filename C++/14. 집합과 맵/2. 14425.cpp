#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, count = 0;
    cin >> n >> m;

    map<string, bool> dictionary;
    string name;
    for (int i = 0; i < n; i++) {
        cin >> name;
        dictionary[name] = true;
    }

    for (int i = 0; i < m; i++) {
        cin >> name;
        if (dictionary.find(name) != dictionary.end())
            count++;
    }

    cout << count;

    return 0;
}