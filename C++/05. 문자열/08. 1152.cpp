#include <stdio.h>
#include <string.h>

int main() {
    int count = 1;
    char str[1000000];
    scanf("%[^\n]%*c", str);

    if (strlen(str) == 0) {
        printf("0");
        return 0;
    }
    if (strlen(str) == 1 && str[0] == ' ') {
        printf("0");
        return 0;
    }

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == ' ')
            count++;
    }

    if (str[0] == ' ')
        count--;
    if (str[strlen(str)-1] == ' ')
        count--;

    printf("%d", count);

    return 0;
}