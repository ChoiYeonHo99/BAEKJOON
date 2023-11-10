#include <stdio.h>
#include <stdlib.h>

int main() {
    char word[5][15];
    for (int i = 0; i < 15; i++)
        for (int j = 0; j < 5; j++)
            word[j][i] = 0;

    for (int i = 0; i < 5; i++)
        scanf("%s", word[i]);

    for (int i = 0; i < 15; i++)
        for (int j = 0; j < 5; j++)
            if (word[j][i] != '\0')
                printf("%c", word[j][i]);

    return 0;
}