#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

    int j;
    double e;
    char t[500];
    
    // Read and save an integer, double, and String to your variables.
    scanf("%d", &j);
    scanf("%lf", &e);
    fgets(t, sizeof(t), stdin);
    fgets(t, sizeof(t), stdin);
    
    // Print the sum of both integer variables on a new line.

    printf ("%d \n", i+j);
    printf ("%.1f \n", d+e);
    printf ("%s%s \n", s, t);
    // Print the sum of the double variables on a new line.

    return 0;
}