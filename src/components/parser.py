
class Node:
    def print_tree(self, file, indent=0):
        raise NotImplementedError("Subclass must implement print_tree method")
    
class AssignmentNode(Node):
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def print_tree(self, file, indent=0):
        file.write('  ' * indent + f'Assignment: {self.id} = {self.value}\n')

class FunctionDeclarationNode(Node):
    def __init__(self, type, id, params, body):
        self.type = type
        self.id = id
        self.params = params
        self.body = body

    def print_tree(self, file, indent=0):
            file.write('  ' * indent + f'Function: {self.id} ({self.type})\n')
            for param in self.params:
                if isinstance(param, str):
                    file.write('  ' * (indent + 1) + param + '\n')
                else:
                    param.print_tree(file, indent + 1)
            for statement in self.body:
                if isinstance(statement, str):
                    file.write('  ' * (indent + 1) + statement + '\n')
                else:
                    statement.print_tree(file, indent + 1)

class VariableDeclarationNode(Node):
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

    def print_tree(self, file, indent=0):
        file.write('  ' * indent + f'Variable: {self.id} ({self.type}) = {self.value}\n')

class ReturnStatementNode(Node):
    def __init__(self, expression):
        self.expression = expression

    def print_tree(self, file, indent=0):
            if isinstance(self.expression, str):
                file.write('  ' * indent + 'Return: ' + self.expression + '\n')
            else:
                file.write('  ' * indent + 'Return:\n')
                self.expression.print_tree(file, indent + 1)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def consume(self, expected_type):
        if self.current < len(self.tokens) and self.tokens[self.current].type == expected_type:
            self.current += 1
        else:
            raise Exception(f'Unexpected token {self.tokens[self.current].value}, expected {expected_type}')

    def parse(self):
        return self.parse_function()

    def parse_function(self):
        self.consume('DATATYPE')
        id = self.tokens[self.current].value
        self.consume('IDENTIFIER')
        self.consume('SEPARATOR')
        self.consume('KEYWORD')
        self.consume('SEPARATOR')
        self.consume('SEPARATOR')
        params = []
        body = []
        while self.tokens[self.current].type != 'SEPARATOR' or self.tokens[self.current].value != '}':
            if self.tokens[self.current].type == 'DATATYPE':
                body.append(self.parse_variable_declaration())
            elif self.tokens[self.current].type == 'IDENTIFIER':
                body.append(self.parse_assignment())
            elif self.tokens[self.current].type == 'KEYWORD':
                body.append(self.parse_return())
        self.consume('SEPARATOR')
        return FunctionDeclarationNode('int', id, params, body)

    def parse_variable_declaration(self):
        type = self.tokens[self.current].value
        self.consume('DATATYPE')
        id = self.tokens[self.current].value
        self.consume('IDENTIFIER')
        self.consume('OPERATOR')
        value = self.parse_expression()
        self.consume('SEPARATOR')
        return VariableDeclarationNode(type, id, value)

    def parse_assignment(self):
        id = self.tokens[self.current].value
        self.consume('IDENTIFIER')
        self.consume('OPERATOR')
        value = self.parse_expression()
        self.consume('SEPARATOR')
        return AssignmentNode(id, value)

    def parse_expression(self):
        if self.tokens[self.current].type == 'IDENTIFIER':
            value = self.tokens[self.current].value
            self.consume('IDENTIFIER')
        elif self.tokens[self.current].type == 'NUMBER':
            value = self.tokens[self.current].value
            self.consume('NUMBER')
        else:
            raise Exception(f"Unexpected token {self.tokens[self.current].type}")

        while self.current < len(self.tokens) and self.tokens[self.current].type == 'OPERATOR':
            operator = self.tokens[self.current].value
            self.consume('OPERATOR')
            if operator == '++':
                value = f"{value}{operator}"
                break
            elif self.tokens[self.current].type == 'IDENTIFIER':
                value2 = self.tokens[self.current].value
                self.consume('IDENTIFIER')
            elif self.tokens[self.current].type == 'NUMBER':
                value2 = self.tokens[self.current].value
                self.consume('NUMBER')
            elif self.tokens[self.current].type == 'SEPARATOR':
                break
            else:
                raise Exception(f"Unexpected token {self.tokens[self.current].type}")
            value = f"{value} {operator} {value2}"

        return value

    def parse_return(self):
        self.consume('KEYWORD')
        value = self.tokens[self.current].value
        self.consume('NUMBER')
        self.consume('SEPARATOR')
        return ReturnStatementNode(value)