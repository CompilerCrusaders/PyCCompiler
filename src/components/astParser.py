# Function: (int) main 
#   Variable: (int) a (operator) = (int) 5
#   Variable: (int) b (operator) = (int) 6
#   Variable: (int) c (operator) = (int) a (operator) + (int) b
#   Assignment: (int) b (operator) = (int) b
#   Assignment: (int) c (operator) = (int) c
#   Variable: (char) symbol1 (operator) = (char) 'x'
#   Return: (int) 0

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

class Node:
    def __init__(self, name, branches):
        self.name = name
        self.branches = branches

    def print_node(self, indent):
        print(indent + self.name)
        for branch in self.branches:
            branch.print_node(indent + "  ")

def draw_tree(ax, node, x, y, dx, dy, level=0, max_levels=None):
    if max_levels is not None and level >= max_levels:
        return

    ax.text(x, y, node.name, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
    
    if node.branches:
        num_branches = len(node.branches)
        next_x = x - dx / 2 + dx / num_branches / 2

        for branch in node.branches:
            ax.add_patch(FancyArrowPatch((x, y - dy / 2), (next_x, y - dy), mutation_scale=15, arrowstyle='->', color='black'))
            draw_tree(ax, branch, next_x, y - dy, dx / num_branches, dy, level + 1, max_levels)
            next_x += dx / num_branches

def plot_tree(root, max_levels=None):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis('off')

    draw_tree(ax, root, 0.5, 1, 3, 0.07, max_levels=max_levels)

    plt.show()

def parse_operator(operator, left, right):

    node = Node("operator", [Node(operator,[])])

    if "operator" in left:
        operatorIndex = str.find(left, "operator")
        operator = left[operatorIndex + 10:operatorIndex + 11]
        leftStart = 0
        leftEnd = operatorIndex - 1
        left = left[leftStart:leftEnd]
        rightStart = operatorIndex + 11
        rightEnd = len(left)
        right = left[rightStart:rightEnd]
        node.branches[0].branches.append(parse_operator(operator.strip(), left.strip(), right.strip()))
    else:
        node.branches[0].branches.append(Node(left.split(" ")[0],[Node(left.split(" ")[1], [])]))

    if "operator" in right:
        operatorIndex = str.find(right, "operator")
        operator = right[operatorIndex + 10:operatorIndex + 11]
        leftStart = 0
        leftEnd = operatorIndex - 1
        left = right[leftStart:leftEnd]
        rightStart = operatorIndex + 11
        rightEnd = len(right)
        right = right[rightStart:rightEnd]
        node.branches[0].branches.append(parse_operator(operator.strip(), left.strip(), right.strip()))
    else:
        node.branches[0].branches.append(Node(right.split(" ")[0],[Node(right.split(" ")[1], [])]))

    return node

def parse_to_ast(input_string):
    masterNode = Node("Program", [Node("Function", [Node("int", [Node("main", [])])])])
    for line in input_string.split("\n")[:-1]:
        if "Function" not in line:
            lineNode = Node("", [])
            words = line.split(" ")
            for word in words:
                if ":" in word:
                    lineNode = Node(word[:-1],[])

            if "operator" in line:
                #find the operator
                operatorIndex = str.find(line, "operator")
                operator = line[operatorIndex + 10:operatorIndex + 11]

                if ":" in line:
                    leftStart = str.find(line, ":") + 1
                else:
                    leftStart = 0

                leftEnd = operatorIndex - 1
                left = line[leftStart:leftEnd]

                rightStart = operatorIndex + 11
                rightEnd = len(line)
                right = line[rightStart:rightEnd]

                operatorNode = parse_operator(operator.strip(), left.strip(), right.strip())
                lineNode.branches.append(operatorNode)
            
            if "Return" in line:
                
                words = line.split(" ")

                returnIndex = words.index("Return:")

                lineNode.branches.append(Node(words[returnIndex+1], [Node(words[returnIndex+2], [])]))


            masterNode.branches[0].branches[0].branches[0].branches.append(lineNode)
                  

    return masterNode

text = ""
with open("src\outputs\AST.txt") as file:
    text = file.read()
    
master = parse_to_ast(text)

master.print_node("")

plot_tree(master, max_levels=15)
