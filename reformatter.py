import sys
import os
import re
from token import Token
file_path = 'src/test/lexertest.c'  # This sets a variable to the directory of our given


# this should remove all the comments, tabs, and white spaces
def reformat(current_file_arg):

    with open(current_file_arg, 'r') as file:  # opens file as readable doc under 'file'
        code = file.read()  # assigns copy of 'file' into 'code'
        lines = code.splitlines()  # makes a list of lines in code

        all_modified_lines = []

        for line in lines:
            modified_line = line.strip()
            # Initialize modifiedLine to the original line without leading/trailing whitespaces
            # Does not account for spaces between

            # Check for // and /* */ comments
            if '//' in modified_line:
                modified_line = modified_line.split('//')[0]  # .split() makes list before and after '//' keeping before
            if '/*' in modified_line:
                modified_line = modified_line.split('/*')[0]
            if '*/' in modified_line:
                modified_line = modified_line.split('*/')[1]

            # Replace tabs with spaces
            modified_line = modified_line.replace('\t', ' ')

            # Add the modified line to the list if it's not empty
            if modified_line.strip():
                all_modified_lines.append(modified_line)

        cleaned_code = '\n'.join(all_modified_lines)  # makes a single string with '\n' between each string

    return cleaned_code


# this should go through all the characters in the file and return the tokens
def lexer(char_list):
    tokens_list = []

    # read/looks for numbers, symbols, operator, variable names, datatypes, keywords, separators respectively
    number_pattern = r'\d+'
    symbol_pattern = r'[=+\-*/%]'
    operator_pattern = r'[=+\-*/%]'
    variable_pattern = r'[a-zA-Z_]\w*'
    datatype_pattern = r'\b(int|float|char|bool)\b'
    keyword_pattern = r'\b(if|else|while|for|return)\b'
    separator_pattern = r'[();{}]'

    # Finds all token classifications in 'char_list'
    number_tokens = re.findall(number_pattern, char_list)
    symbol_tokens = re.findall(symbol_pattern, char_list)
    operator_tokens = re.findall(operator_pattern, char_list)
    variable_tokens = re.findall(variable_pattern, char_list)
    datatype_tokens = re.findall(datatype_pattern, char_list)
    keyword_tokens = re.findall(keyword_pattern, char_list)
    separator_tokens = re.findall(separator_pattern, char_list)

    # for loops through tokens and files them into Token class tuple
    for number in number_tokens:
        tokens_list.append(Token('NUMBER', int(number)))
    for symbol in symbol_tokens:
        tokens_list.append(Token('SYMBOL', symbol))
    for operator in operator_tokens:
        tokens_list.append(Token('OPERATOR', operator))
    for identifier in variable_tokens:
        tokens_list.append(Token('IDENTIFIER', identifier))
    for d_type in datatype_tokens:
        tokens_list.append(Token('DATATYPE', d_type))
    for keyword in keyword_tokens:
        tokens_list.append(Token('KEYWORD', keyword))
    for separator in separator_tokens:
        tokens_list.append(Token('SEPARATOR', separator))

    # Following helps troubleshoot and error-handling

    # re.sub subs all white space with '' in char list
    remaining_chars = re.sub(r'\s+', '', char_list)  # Remove whitespace for checking unexpected characters
    if remaining_chars:
        raise ValueError(f"Unexpected characters: {remaining_chars}")  # f-strings concatenates without the need of '+'
    # 'raise ValueError' allows custom error message from built in 'ValueError' when key is correct but value wrong
    return tokens_list


with open(file_path, 'r') as file:
    charList = file.read()  # this is a string of all the characters in the file
    print(charList)
reformattedFile = reformat(file_path)

with open('src/test/processedc.txt', 'w') as file:
    file.write(reformattedFile)