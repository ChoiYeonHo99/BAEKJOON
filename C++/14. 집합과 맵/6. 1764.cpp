#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, count = 0;
    cin >> n >> m;

    string name;
    map<string, bool> dictionary;
    for (int i = 0; i < n; i++) {
        cin >> name;
        dictionary[name] = false;
    }

    for (int i = 0; i < m; i++) {
        cin >> name;
        if (dictionary.find(name) != dictionary.end()) {
            count++;
            dictionary[name] = true;
        }
    }

    cout << count << '\n';
    for (auto iter = dictionary.begin(); iter != dictionary.end(); iter++)
        if (iter->second)
            cout << iter->first << '\n';

    return 0;
}