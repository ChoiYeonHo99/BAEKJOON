#include <stdio.h>

int main() {
    int n, m, left, right, temp;
    scanf("%d %d", &n, &m);
  
    int arr[101] = {};
    for (int i = 1; i < n+1; i++) {
        arr[i] = i;
    }

    for (int i = 0; i < m; i++) {
        scanf("%d %d", &left, &right);
        while (1) {
            if (left >= right) {
                break;
            }
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left += 1;
            right -= 1;
        }
    }

    for (int i = 1; i < n+1; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}