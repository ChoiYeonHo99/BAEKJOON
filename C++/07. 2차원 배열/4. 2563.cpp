#include <stdio.h>
#include <stdlib.h>

int main() {
    int** a;
    int n, x, y, result = 0;
    a = (int**)malloc(sizeof(int*) * 100);
    for (int i = 0; i < 100; i++) {
        a[i] = (int*)malloc(sizeof(int) * 100);
        for (int j = 0; j < 100; j++)
            a[i][j] = 0;
    }

    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%d %d", &x, &y);
        for (int i = x-1; i < x+9; i++)
            for (int j = y-1; j < y+9; j++)
                a[i][j] = 1;
    }

    for (int i = 0; i < 100; i++)
        for (int j = 0; j < 100; j++)
            if (a[i][j] == 1)
                result++;

    printf("%d", result);

    return 0;
}