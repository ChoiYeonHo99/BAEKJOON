#include <stdio.h>

int main() {
    int n, x, result = 0;
  
    int arr[42] = {};
    for (int i = 0; i < 10; i++) {
        scanf("%d", &n);
        x = n % 42;
        arr[x] += 1;
    }

    for (int i = 0; i < 42; i++) {
        if (arr[i] != 0) {
            result += 1;
        }
    }
    printf("%d", result);

    return 0;
}