#include <stdio.h>

int main() {
    char operator;
    double num1, num2, result;

    // Use a while loop to allow for multiple calculations until the user chooses to exit.
    while (1) {
        // Prompt user to enter an operator
        printf("\nEnter an operator (+, -, *, /). Enter 'q' to quit: ");
        scanf(" %c", &operator);

        // Check if the user wants to quit
        if (operator == 'q' || operator == 'Q') {
            printf("Exiting the calculator. Goodbye!\n");
            break;
        }

        // Prompt user to enter two numbers
        printf("Enter two numbers separated by a space: ");
        if (scanf("%lf %lf", &num1, &num2) != 2) {
            printf("Invalid input. Please enter numbers.\n");
            // Clear the input buffer to prevent an infinite loop
            while(getchar() != '\n');
            continue;
        }
        
        // Use a switch statement to perform the calculation based on the operator
        switch (operator) {
            case '+':
                result = num1 + num2;
                printf("%.2lf + %.2lf = %.2lf\n", num1, num2, result);
                break;
            case '-':
                result = num1 - num2;
                printf("%.2lf - %.2lf = %.2lf\n", num1, num2, result);
                break;
            case '*':
                result = num1 * num2;
                printf("%.2lf * %.2lf = %.2lf\n", num1, num2, result);
                break;
            case '/':
                // Check for division by zero
                if (num2 != 0) {
                    result = num1 / num2;
                    printf("%.2lf / %.2lf = %.2lf\n", num1, num2, result);
                } else {
                    printf("Error! Division by zero is not allowed.\n");
                }
                break;
            default:
                // Operator doesn't match any case
                printf("Error! The operator '%c' is not valid.\n", operator);
                break;
        }
    }

    return 0;
}