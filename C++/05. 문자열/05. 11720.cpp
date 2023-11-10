#include <stdio.h>

int main() {
    int n, total = 0;
    scanf("%d", &n);

    char str[n];
    scanf("%s", str);

    for (int i = 0; i < n; i++) {
        total += str[i] - 48;
    }
    printf("%d", total);

    return 0;
}