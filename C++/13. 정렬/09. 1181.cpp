#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int cmp(string s1, string s2) {
  if (s1.length() == s2.length())
    return s1 < s2;
  else
    return s1.length() < s2.length();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr, arr + n, cmp);

    for (int i = 0; i < n; i++) {
        if (i > 0 && arr[i] == arr[i-1])
            continue;

        cout << arr[i] << "\n";
    }

    return 0;
}