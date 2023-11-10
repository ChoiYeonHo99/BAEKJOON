#include <stdio.h>

int main() {
    int a, b, p3, p4, p5, p6;

    scanf("%d", &a);
    scanf("%d", &b);

    p3 = b % 10;
    printf("%d\n", a * p3);
    p4 = (b % 100 - p3) / 10;
    printf("%d\n", a * p4);
    p5 = b / 100;
    printf("%d\n", a * p5);
    printf("%d", a * b);

    return 0;
}