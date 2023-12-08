import components.lexer as lexer
from components.parser import Parser
from components.tokenClass import Token
import components.astParser as astParser
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

with open("./src/outputs/AST.txt", 'w') as outputFile:
    ast.print_tree(outputFile)
with open("./src/outputs/AST.txt", 'r') as outputFile:  
    astMasterNode = astParser.parse_to_ast(outputFile.read())


astParser.plot_tree(astMasterNode, max_levels=15)
astMasterNode.saveNode("./src/outputs/AST.json")



