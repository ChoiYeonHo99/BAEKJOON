#include <stdio.h>

int main() {
    int n, m, a, b, temp;
    scanf("%d %d", &n, &m);
  
    int arr[101] = {};
    for (int i = 1; i < n+1; i++) {
        arr[i] = i;
    }
  
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a, &b);
        temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    for (int i = 1; i < n+1; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}