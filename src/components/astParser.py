# Function: (int) main 
#   Variable: (int) a (operator) = (int) 5
#   Variable: (int) b (operator) = (int) 6
#   Variable: (int) c (operator) = (int) a (operator) + (int) b
#   Assignment: (int) b (operator) = (int) b
#   Assignment: (int) c (operator) = (int) c
#   Variable: (char) symbol1 (operator) = (char) 'x'
#   Return: (int) 0

import re

class Node:
    def __init__(self, name, branches):
        self.name = name
        self.branches = branches

    def print_node(self, indent):
        print(indent + self.name)
        for branch in self.branches:
            branch.print_node(indent + "  ")

def parse_operator(input_string):
    pass

def parse_to_ast(input_string):
    masterNode = Node("Program", [Node("Function", [Node("int", [Node("main", [])])])])
    for line in input_string.split("\n"):
        if "Function" not in line:
            lineNode = Node("", [])
            words = line.split(" ")
            for word in words:
                if ":" in word:
                    lineNode = Node(word[:-1],[])

            if "operator" in line:
                operationNode = Node("", [])
                for word in words:
                    if "operator" in word:
                        operationNode = Node(word[1:-1], [])
                        nextWord = words[words.index(word) + 1]
                        operationNode.branches.append(Node(nextWord, []))

                for word in words:
                    if "(" in word and "operator" not in word:
                        operationNode.branches[0].branches.append(Node(word[1:-1], []))
                        
                    
                lineNode.branches.append(operationNode)
            
            masterNode.branches[0].branches[0].branches[0].branches.append(lineNode)
                  

    return masterNode

text = ""
with open("src\outputs\AST.txt") as file:
    text = file.read()

print(text)
    
master = parse_to_ast(text)

master.print_node("")