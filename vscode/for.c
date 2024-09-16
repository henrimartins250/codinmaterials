#include <stdio.h>

int main(){
    int i;   
   // i = 0 by default  
printf("HERES your list from 1 to 100:\n\n");
for(i=0; i <= 100; i++){
    printf("%d\n", i);
}
/*
Expression 1 sets a variable before the loop starts (int i = 0).
Expression 2 defines the condition for the loop to run (i must be less than 5).
 If the condition is true,the loop will start over again, if it is false, the loop will end.
Expression 3 increases a value (i++) each time the code block in the loop has been executed.
*/
return 0;
}