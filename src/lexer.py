#Lexer to do list
# 1. Read the input file
# 2. Remove all the comments
# 3. Remove all the white spaces
# 4. Identify all the tokens
# 5. Return the tokens
# 6. Return the errors if any

#token types
# 1. symbols
# 2. numbers
# 3. = - + * / %
# 4. () {} [] ; , .
# 5. individuals variable types
# 6. loops
# 15. switch
# 16. comments

import sys
import os

file_path = 'src/test/lexertest.c'

def reformat(charList): # this should remove all the comments and white spaces
    #NOTE: there are specific circumstances where you do want white space, so it would be beneficial to keep spaces and things
    #      relevant things to get rid of would be things like spaces between lines and comments; if theres something im forgetting just add it
    return;

def lexer(charList): # this should go through all the characters in the file and return the tokens
    return;

with open(file_path, 'r') as file:
    charList = file.read() # this is a string of all the characters in the file
    print(charList)


