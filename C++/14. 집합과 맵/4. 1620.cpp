#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    map<string, string> dictionary;
    string name, order, target;
    for (int i = 0; i < n; i++) {
        cin >> name;
        order = to_string(i + 1);
        dictionary[name] = order;
        dictionary[order] = name;
    }

    for (int i = 0; i < m; i++) {
        cin >> target;
        cout << dictionary[target] << '\n';
    }

    return 0;
}