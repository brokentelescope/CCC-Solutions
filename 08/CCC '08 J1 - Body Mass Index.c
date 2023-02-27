#include <stdio.h>

int main() {

    float weight = 0;
    float height = 0;
    float bmi = 0;

    scanf("%f", &weight);
    scanf("%f", &height);

    bmi = weight/(height*height);

    if (bmi > 25.0) {
        printf("Overweight");
    }

    else if (bmi >= 18.5 & bmi <= 25.0) {
        printf("Normal weight");
    }

    else {
        printf("Underweight");
    }
}
