#include <stdbool.h>
#include <stdio.h>

int main(){
    bool s = false;
    int numero;
    
    int  odd = 0, even = 0;

    printf("type a number\n\n");
    scanf("%d", &numero);
    printf("%d, ok\n", numero);

    int counter = 0; 
while(s == false){
    for (counter = 0; counter <= numero; counter++ ){
        if(counter % 2 == 0) {
            even =+ even + counter;
        }
            else{
                s = true;
        }
    }
}

counter = 0;
while(s == true){
    for (counter >= 0; counter <= numero; counter++) {
        if(counter % 2 == 1) {
            odd =+ odd + counter;
        }
        else{
            s = false;
        }
    }
}
printf("odds: %d\n", odd);
printf("evens: %d\n", even);

return 0;
}