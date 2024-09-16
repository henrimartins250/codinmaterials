#include <stdio.h>

int main(){
    int order;
    char name[25];

    printf("hello! whats your name?\n\n");
    scanf("%s", name);

    printf("hi %s how are you\n\n",name);
    printf("here's the menu for our hamberguers\n\n");

    printf("1 chesseburger, \"beef patty, chesse, mayo, lettuce, toamtoes, gergelin bread\"\n\n 2 hamburguer, \"beef patty, onions, chesse, ketchup, mayo, lettuce, tomatoes,\"\n\n3 super, \"beef patty, eggs, ham, cheese, tomatoes, lettuce, mayo, ketchp, tasty sauce,\"\n\n");
    scanf("%d", &order);

    switch (order) {
    case 1:
    printf("\n\nheres your cheeseburguer\n\n");
    break;
    case 2:
    printf("\n\nheres your cheeseburguer\n\n");
    break;
    case 3:
    printf("\n\nheres your cheeseburguer\n\n");
    break;
    default:
    printf("\n\nsorry we dont have that option\n\n");
    break;
    }
    return 0;
    }
