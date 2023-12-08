import json

def generate_assembly(node):
    nodeName = node['name']

    if nodeName == "Program":
        

    print(nodeName)

print(generate_assembly(json.load(open('./src/outputs/AST.json'))))