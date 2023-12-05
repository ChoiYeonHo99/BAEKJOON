#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> arr(n), sorted(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        sorted[i] = arr[i];
    }

    sort(sorted.begin(), sorted.end());
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());

    for (int i = 0; i < n; i++) 
        cout << lower_bound(sorted.begin(), sorted.end(), arr[i]) - sorted.begin() << " ";
}