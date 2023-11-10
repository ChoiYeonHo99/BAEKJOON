#include <stdio.h>
#include <string.h>

float GradeTransducer(char *score) {
    if (strcmp(score, "A+") == 0)
        return 4.5;
    else if (strcmp(score, "A0") == 0)
        return 4.0;
    else if (strcmp(score, "B+") == 0)
        return 3.5;
    else if (strcmp(score, "B0") == 0)
        return 3.0;
    else if (strcmp(score, "C+") == 0)
        return 2.5;
    else if (strcmp(score, "C0") == 0)
        return 2.0;
    else if (strcmp(score, "D+") == 0)
        return 1.5;
    else if (strcmp(score, "D0") == 0)
        return 1.0;
    return 0;
}

int main() {
    float credit, totalCredit = 0, totalScore = 0;
    char subject[50], score[2];

    for (int i = 0; i < 20; i++) {
        scanf("%s %f %s", subject, &credit, score);
        if (score[0] == 'P')
            continue;

        totalCredit += credit;
        totalScore += credit * GradeTransducer(score);
    }

    printf("%f", totalScore / totalCredit);

    return 0;
}