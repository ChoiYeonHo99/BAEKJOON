#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 9, maxValue = -1, x, y;
    int** a;
    a = (int**)malloc(sizeof(int*) * n);

    for (int i = 0; i < n; i++) {
        a[i] = (int*)malloc(sizeof(int) * n);
        for (int j = 0; j < n; j++) {
            scanf("%d", &a[i][j]);
            if (maxValue < a[i][j]) {
                maxValue = a[i][j];
                x = i+1;
                y = j+1;
            }
        }
    }

    printf("%d\n%d %d", maxValue, x, y);

    return 0;
}