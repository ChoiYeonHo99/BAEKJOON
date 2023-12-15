#include <iostream>
#include <list>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, a, count[8001] = {0}, maxCount = 0, index = 0;
    double sum = 0;
    cin >> n;

    int arr[500000];
    int frequency[500000];

    for (int i = 0; i < n; i++) {
        cin >> a;
        sum += (double)a;
        arr[index] = a;
        index++;
        if (a < 0)
            count[a + 8001]++;
        else
            count[a]++;
    }
    
    for (int i = 0; i < 8001; i++)
        if (maxCount < count[i])
            maxCount = count[i];
    index = 0;
    for (int i = 0; i < 8001; i++) {
        if (count[i] == maxCount) {
            if (i > 4000)
                frequency[index] = i - 8001;
            else
                frequency[index] = i;
            index++;
        }
    }

    sort(arr, arr + n);
    sort(frequency, frequency + index);

    cout << floor(sum / n + 0.5) << '\n';
    cout << arr[n / 2] << '\n';
    if (index > 1)
        cout << frequency[1] << '\n';
    else
        cout << frequency[0] << '\n';
    cout << arr[n - 1] - arr[0];
    
    return 0;
}