import sys
import os
import re
from components.tokenClass import Token
file_path = 'src/test/lexertest.c'  # This sets a variable to the directory of our given


def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)


# this should remove all the comments, tabs, and white spaces
def reformat(code):
    
    reformattedCode = remove_comments(code)

    reformattedLines = []

    # remove blank lines
    for line in reformattedCode.splitlines():
        if line.strip() != '':
            reformattedLines.append(line.strip())
            
    reformattedCode = '\n'.join(reformattedLines)

    return reformattedCode

def create_tokens(token_type, tokens, tokens_list):
    for token in tokens:
        tokens_list.append(Token(token_type, token))

operator_tokens = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=', '++', '--', '+=', '-=', '*=', '/=', '%=', '<<', '>>', '&', '|', '^', '&&', '||', '!', '~', '%', '->', '.', '?:']
datatype_tokens = ['int', 'float', 'char', 'double', 'long']
keyword_tokens = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
separator_tokens = ['(', ')', '{', '}', '[', ']', ';', ',']

def lex(code):
    # Split the code into words and symbols
    words_and_symbols = re.findall(r'\".*?\"|\b\w+\b|==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|%=|<<|>>|&&|\|\||\S', code)
    tokens_list = []
    for i in range(len(words_and_symbols)):
        word_or_symbol = words_and_symbols[i]
        if word_or_symbol in operator_tokens:
            tokens_list.append(Token('OPERATOR', word_or_symbol))
        elif i < len(words_and_symbols) - 2 and words_and_symbols[i+1] == '(' and word_or_symbol in datatype_tokens:  # This is a regex for function declarations
            tokens_list.append(Token('FUNCTION', words_and_symbols[i+1]))
            i += 2  # Skip the next two symbols, because we've already processed them
        elif word_or_symbol in datatype_tokens:
            tokens_list.append(Token('DATATYPE', word_or_symbol))
        elif word_or_symbol in keyword_tokens:
            tokens_list.append(Token('KEYWORD', word_or_symbol))
        elif word_or_symbol in separator_tokens:
            tokens_list.append(Token('SEPARATOR', word_or_symbol))
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word_or_symbol):  # This is a regex for variable identifiers
            tokens_list.append(Token('IDENTIFIER', word_or_symbol))
        elif re.match(r'^\d+(\.\d*)?([eE][+-]?\d+)?$', word_or_symbol):  # This is a regex for numeric literals
            tokens_list.append(Token('NUMBER', word_or_symbol))
        elif re.match(r'^\".*\"$', word_or_symbol):  # This is a regex for strings
            tokens_list.append(Token('STRING', word_or_symbol))

    return tokens_list
