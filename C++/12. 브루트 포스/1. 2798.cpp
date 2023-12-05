#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int num[n], max = 0;
    for (int i = 0; i < n; i++)
        cin >> num[i];

    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                int val = num[i] + num[j] + num[k];

                if (val <= m && val > max)
                    max = val;
            }
        }
    }

    cout << max << endl;
    
    return 0;
}