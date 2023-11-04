int main(void){

    /*This is a multiline comment
    yo

    
    this should not show up at all*/

    int a = 5; //this line should return 5 tokens
    int b = 6; //this line should return 5 tokens
    int c = a + b; //this line should return 9 tokens
    c = c++; //this line should return 5-6 tokens (depends on how we want to handle ++)

    char descriptiveSymbol[] = " /* can you read me? \t \n */"; //this line should return a lot of tokens

    return 0; //this line should return 3 tokens 
}