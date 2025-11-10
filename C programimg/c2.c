// Program to check if you are eligble for vote. Using if,else, else if

#include <stdio.h>
int main()
{
    char name[30];
    int age;

    printf("Enter your Name:");
    scanf("%s", name);

    printf("Enter your Age:");
    scanf("%d",&age);   

    if(age > 18) {
        printf("%s is eligble for Vote.",name);
    }
    else if(age > 13 ){
        printf("You are a Teenager");
    }
    else if(age < 13 ){
        printf("Sorry! You are a Kid.");
    }

    else {
        printf("%s is not eligble for Vote.\n",name);
    }

    printf("\nThanks for Your Controbution");
    
    return 0;
}
