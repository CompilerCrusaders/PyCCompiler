import components.lexer as lexer
from components.parser import Parser
from components.tokenClass import Token
import os

testFile = "./src/test/lexertest.c"

rawCode = ""
with open(testFile, 'r') as file:
    rawCode = file.read()

reformattedCode = lexer.reformat(rawCode)

with open("./src/outputs/ReformattedC.txt", 'w') as outputFile:
    outputFile.write(reformattedCode)

lexRawOutput = lexer.lex(reformattedCode)

lexOutput = ""
for token in lexRawOutput:
    lexOutput += str(token) + "\n"

with open("./src/outputs/LexedC.txt", 'w') as outputFile:
    outputFile.write(lexOutput)

tokens = []
for token in lexRawOutput:
    tokens.append(Token(token.type, token.value))

parser = Parser(tokens)
ast = parser.parse()
file = open("./src/outputs/AST.txt", "w")
print(ast.print_tree(file))
file.close()


