#include <stdio.h>

int main() {
    int n, m, i, j, k;
    scanf("%d %d", &n, &m);
    int arr[101] = {};
    for (int a = 0; a < m; a++) {
        scanf("%d %d %d", &i, &j, &k);
        for (int b = i; b < j+1; b++) {
            arr[b] = k;
        }
    }

    for (int a = 1; a < n+1; a++) {
        printf("%d ", arr[a]);
    }

    return 0;
}