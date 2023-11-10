#include <stdio.h>

int main() {
    int n;
    float sum = 0, max = 0;
    scanf("%d", &n);

    float arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%f", &arr[i]);
        if (max < arr[i]) {
            max = arr[i];
        }
    }

    for (int i = 0; i < n; i++) {
        sum += arr[i] / max * 100;
    }

    printf("%f", sum / n);

    return 0;
}