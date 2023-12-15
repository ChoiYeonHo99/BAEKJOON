#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

bool cmp(pair<string, int> a, pair<string, int> b) {
    if (a.second == b.second) {
        if (a.first.length() == b.first.length())
            return a.first < b.first;

        return a.first.length() > b.first.length();
    }

    return a.second > b.second;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    map<string, int> v;
    while (n--) {
        string w;
        cin >> w;
        if (w.length() >= m)
            v[w]++;
    }

    vector<pair<string, int>> myVector(v.begin(), v.end());
    sort(myVector.begin(), myVector.end(), cmp);

    for (auto p : myVector)
        cout << p.first << "\n";

    return 0;
}