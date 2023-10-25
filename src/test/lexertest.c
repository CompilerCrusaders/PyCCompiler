#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

    /*This is a multiline comment
    this should not show up at all*/

    int a = 5; //this line should return 5 tokens
    int b = 6; //this line should return 5 tokens
    int c = a + b; //this line should return 9 tokens
    c = c++; //this line should return 5-6 tokens (depends on how we want to handle ++)

    char descriptiveSymbol[] = "can you read me?"; //this line should return a lot of tokens

    for i in range(1, 5):
        print("this is python code inside of a c file! uh oh! this should be dealt with in the parser")

    return 0; //this line should return 3 tokens 
}