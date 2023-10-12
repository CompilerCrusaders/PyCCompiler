#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

    int a = 5; //this line should return 5 tokens
    int b = 6; //this line should return 5 tokens
    int c = a + b; //this line should return 9 tokens
    c = c++; //this line should return 5-6 tokens (depends on how we want to handle ++)

    char descriptiveSymbol[] = "can you read me?"; //this line should return a lot of tokens

    return 0; //this line should return 3 tokens 
}