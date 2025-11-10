#include <stdio.h>
int main()
{   
    // In char yyou must add the char length in [ ].
    char name[20];
    int age;

    // Input from user string 
    printf("Enter your Name:");
    scanf("%s", name);

    // Input from user integer 
    printf("Enter your Age:");
    scanf("%d",&age);

    // Print the output in screen.
    printf("Your Name is  %s, and your are %d years old.",name,age);

    return 0;
}