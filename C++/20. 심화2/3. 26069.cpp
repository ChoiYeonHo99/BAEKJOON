#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    set<string> mySet;
    mySet.insert("ChongChong");
    string name1, name2;
    for (int i = 0; i < n; i++) {
        cin >> name1 >> name2;

        if (mySet.find(name1) != mySet.end())
            mySet.insert(name2);
        else if (mySet.find(name2) != mySet.end())
            mySet.insert(name1);
    }

    cout << mySet.size();

    return 0;
}