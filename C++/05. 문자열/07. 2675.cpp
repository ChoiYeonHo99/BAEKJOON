#include <stdio.h>

int main() {
    int t, n;
    char str[20];
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        scanf("%s", str);
        for (int j = 0; j < 20; j++) {
            if (str[j] == '\0')
                break;
            for (int k = 0; k < n; k++) {
                printf("%c", str[j]);
            }
        }
        printf("\n");
    }

    return 0;
}