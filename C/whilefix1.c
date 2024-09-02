
#include <stdbool.h>
#include <stdio.h>

int main() {
    bool s = false;
    int numero, counter;
    int odd = 0, even = 0;

    // Prompt user and read input
    printf("Type a number:\n");
    scanf("%d", &numero);  // Use & to get the address of 'numero'

    // Process even numbers
    counter = 0;
    while (counter <= numero) {
        if (counter % 2 == 0) {
            even += counter;  // Add to even sum
        }
        counter++;
    }

    // Reset the counter and flag to process odd numbers
    counter = 0;
    s = true;  // Set the flag to indicate we are now processing odd numbers

    while (counter <= numero) {
        if (counter % 2 == 1) {
            odd += counter;  // Add to odd sum
        }
        counter++;
    }

    // Print results
    printf("Odds: %d\n", odd);
    printf("Evens: %d\n", even);

    return 0;
    
}
