#include <stdio.h>

int main(){
    int num, res;

    printf("write a number\n\n");
    scanf("%d", &num);

    printf("here is your number %d \n\n", num,"\n\n");

    res = num % 2;

    if(res > 0){
        printf("your number is an odd number\n\n");
    }
    else{
        printf("your number is an even number\n\n");
    }



    return 0;

}


