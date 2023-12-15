#include <iostream>

using namespace std;

int count = 0;

int recursion(string &s, int l, int r) {
    count++;
    if (l >= r)
        return 1;
    else if (s[l] != s[r])
        return 0;
    else
        return recursion(s, l + 1, r - 1);
}

int isPalindrome(string s) {
    return recursion(s, 0, s.length() - 1);
}

int main() {
    int t;
    cin >> t;

    string s;
    for (int i = 0; i < t; i++) {
        count = 0;

        cin >> s;

        cout << isPalindrome(s) << ' ' << count << '\n';
    }

    return 0;
}