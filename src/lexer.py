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
import re

file_path = 'src/test/lexertest.c'

def reformat(file_path): # this should remove all the comments, tabs, and white spaces

    with open(file_path, 'r') as file:
        code = file.read()
        lines = code.splitlines()

        
        modifiedLines = []

        for line in lines:
            modifiedLine = line.strip()  # Initialize modifiedLine to the original line without leading/trailing whitespaces

            # Check for // and /* */ comments
            if '//' in modifiedLine:
                modifiedLine = modifiedLine.split('//')[0]
            if '/*' in modifiedLine:
                modifiedLine = modifiedLine.split('/*')[0]
            if '*/' in modifiedLine:
                modifiedLine = modifiedLine.split('*/')[1]

            # Replace tabs with spaces
            modifiedLine = modifiedLine.replace('\t', ' ')

            # Add the modified line to the list if it's not empty
            if modifiedLine.strip():
                modifiedLines.append(modifiedLine)

        cleaned_code = '\n'.join(modifiedLines)

    return cleaned_code

def lexer(processedCode): # this should go through all the characters in the reformatted file and return the tokens
    return;

reformattedFile = reformat(file_path)
    
with open('src/test/processedc.txt', 'w') as file:
    file.write(reformattedFile)


