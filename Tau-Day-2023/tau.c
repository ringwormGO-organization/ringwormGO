#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double calculate_pi(int n)
{
    double pi = 0.0;
    int i;

    for (i = 0; i < n; i++)
    {
        pi += (1.0 / pow(16, i)) * (4.0 / (8 * i + 1) -
                                    2.0 / (8 * i + 4) -
                                    1.0 / (8 * i + 5) -
                                    1.0 / (8 * i + 6));
    }

    return pi;
}

int main()
{
    printf("=== Happy 𝜏 Day === \n");
    printf("=== Possible approximation === \n");
    printf("Enter radius of circle (cm): ");

    char *radius_input = (char *)malloc(sizeof(char) * 1024);
    scanf("%s", radius_input);

    double pi = calculate_pi(48);
    printf("\nπ ≈ %.48f\n", pi);

    double c = 2.0 * pi * atof(radius_input);
    printf("𝜏 ≈ %.48f\n", (c / atof(radius_input)));

    free(radius_input);
    return 0;
}
