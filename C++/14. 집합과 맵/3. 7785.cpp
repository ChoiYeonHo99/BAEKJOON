#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    map<string, bool> dictionary;
    string name, commute;
    for (int i = 0; i < n; i++) {
        cin >> name >> commute;
        if (commute == "enter")
            dictionary[name] = true;
        else
            dictionary[name] = false;
    }

    for (auto iter = dictionary.rbegin(); iter != dictionary.rend(); iter++)
        if (iter->second)
            cout << iter->first << '\n';

    return 0;
}