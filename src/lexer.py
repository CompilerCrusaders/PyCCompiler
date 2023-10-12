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

test_folder = "/test"
test_file = "/test/lexertest.c"
file_path = os.path.join(test_folder, test_file)

def lexer(charList): # this should go through all the characters in the file and return the tokens
    return;
