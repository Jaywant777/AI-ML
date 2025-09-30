#include <stdio.h>
int main () {
    float p,r,t;

    printf("Enter amount:");
    scanf("%f",&p);

    printf("Enter intrest rate:");
    scanf("%f",&r);

    printf("Enter duration:");
    scanf("%f",&t);
       
    float interest= (p*r*t)/100.0;
    printf("Your per annum intrest is %.2f\n1",&interest);


    return 0;

}