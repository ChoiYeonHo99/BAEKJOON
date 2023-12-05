#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool cmp(pair<int, int> v1, pair<int, int> v2) {
    if (v1.first == v2.first)
        return v1.second < v2.second;

    return v1.first < v2.first;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<pair<int, int>> v;
    int age;
    string name[n];
    for (int i = 0; i < n; i++) {
        cin >> age >> name[i];
        v.push_back({age, i});
    }

    sort(v.begin(), v.end(), cmp);

    for (int i = 0; i < n; i++)
        cout << v[i].first << " " << name[v[i].second] << '\n';

    return 0;
}