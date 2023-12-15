#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, result = 0;
    cin >> n;

    set<string> mySet;
    string name;
    for (int i = 0; i < n; i++) {
        cin >> name;
        if (name == "ENTER") {
            result += mySet.size();
            mySet.clear();
        }
        else
            mySet.insert(name);
    }

    result += mySet.size();
    cout << result;

    return 0;
}