#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    set<string> mySet;
    for (int i = 0; i < s.length(); i++)
        for (int j = 0; j < s.length() - i; j++)
            mySet.insert(s.substr(j, i + 1));

    cout << mySet.size();

    return 0;
}