#include <map>
#include <stdio.h>
#include <string>
using namespace std;

int main() {
    int maxValue = 0;
    char maxChar;
    char str[1000000];
    scanf("%s", str);

    map<char, int> myMap;
    for (int i = 0; str[i] != '\0'; i++) {
        myMap[tolower(str[i])]++;
    }

    for (auto iter : myMap) {
        if (maxValue < iter.second) {
            maxValue = iter.second;
            maxChar = toupper(iter.first);
        }
        else if (maxValue == iter.second) {
            maxValue = iter.second;
            maxChar = '?';
        }
    }

    printf("%c", maxChar);

    return 0;
}