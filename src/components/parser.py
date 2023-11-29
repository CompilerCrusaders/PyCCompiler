
class Node:
    def print_tree(self, file, indent=0):
        raise NotImplementedError("Subclass must implement print_tree method")
    
class AssignmentNode(Node):
    def __init__(self, type, id, value):
        self.id = id
        self.value = value
        self.type = type

    def print_tree(self, file, indent=0):
        file.write('  ' * indent + f'Assignment: ({self.type}) {self.id} (operator) = {self.value}\n')

class FunctionDeclarationNode(Node):
    def __init__(self, type, id, params, body, symbol_table):
        self.type = type
        self.id = id
        self.params = params
        self.body = body
        symbol_table[id] = type

    def print_tree(self, file, indent=0):
            file.write('  ' * indent + f'Function: ({self.type}) {self.id} \n')
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
    def __init__(self, type, id, value, symbol_table):
        self.type = type
        self.id = id
        self.value = value
        symbol_table[id] = type

    def print_tree(self, file, indent=0):
        file.write('  ' * indent + f'Variable: ({self.type}) {self.id} (operator) = {self.value}\n')

class ReturnStatementNode(Node):
    def __init__(self, type, expression):
        self.expression = expression
        self.type = type

    def print_tree(self, file, indent=0):
            if isinstance(self.expression, str):
                file.write('  ' * indent + f'Return: ({self.type}) ' + self.expression + '\n')
            else:
                file.write('  ' * indent + f'Return: ({self.type})\n')
                self.expression.print_tree(file, indent + 1)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.symbol_table = {}

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
        return FunctionDeclarationNode('int', id, params, body, self.symbol_table)

    def parse_variable_declaration(self):
        type = self.tokens[self.current].value
        self.consume('DATATYPE')
        id = self.tokens[self.current].value
        self.consume('IDENTIFIER')
        self.consume('OPERATOR')
        value = self.parse_expression()
        self.consume('SEPARATOR')
        self.symbol_table[id] = type  # Add the variable and its type to the symbol table
        return VariableDeclarationNode(type, id, value, self.symbol_table)

    def parse_assignment(self):
        id = self.tokens[self.current].value
        self.consume('IDENTIFIER')
        self.consume('OPERATOR')
        value = self.parse_expression()
        self.consume('SEPARATOR')
        type = self.symbol_table.get(id, None)
        return AssignmentNode(type, id, value)

    def parse_expression(self):
        if self.tokens[self.current].type == 'IDENTIFIER':
            id = self.tokens[self.current].value
            type = self.symbol_table.get(id, None)
            if type is None:
                print(type)
                raise Exception(f"Undefined variable {id}")
            value = f'({type}) {id}'
            self.consume('IDENTIFIER')
        elif self.tokens[self.current].type == 'NUMBER':
            value = f'(int) {self.tokens[self.current].value}'
            self.consume('NUMBER')
        elif self.tokens[self.current].type == 'CHAR':
            value = f'(char) {self.tokens[self.current].value}'
            self.consume('CHAR')
        else:
            raise Exception(f"Unexpected token {self.tokens[self.current].type}")

        while self.current < len(self.tokens) and self.tokens[self.current].type == 'OPERATOR':
            operator = self.tokens[self.current].value
            self.consume('OPERATOR')
            if operator == '++':
                value = f"{value} (operator) + (int) 1"
                break
            elif operator == '--':
                value = f"{value} (operator) - (int) 1"
                break
            elif self.tokens[self.current].type == 'IDENTIFIER':
                id = self.tokens[self.current].value
                type = self.symbol_table.get(id, None)
                value2 = f'({type}) {id}'
                self.consume('IDENTIFIER')
            elif self.tokens[self.current].type == 'NUMBER':
                value2 = f'(int) {self.tokens[self.current].value}'
                self.consume('NUMBER')
            elif self.tokens[self.current].type == 'CHAR':
                value2 = f'(char) {self.tokens[self.current].value}'
                self.consume('CHAR')
            elif self.tokens[self.current].type == 'SEPARATOR':
                break
            else:
                raise Exception(f"Unexpected token {self.tokens[self.current].type}")
            value = f"{value} (operator) {operator} {value2}"

        return value

    def parse_return(self):
        self.consume('KEYWORD')
        value = self.tokens[self.current].value
        original_type = self.tokens[self.current].type  # Get the type before consuming the token
        self.consume(original_type)  # Consume the token
        type_mapping = {'NUMBER': 'int', 'STRING': 'str', 'IDENTIFIER': 'var'}  # Mapping dictionary
        type = type_mapping.get(original_type, original_type)  # Convert the type using the dictionary
        self.consume('SEPARATOR')
        return ReturnStatementNode(type, value)