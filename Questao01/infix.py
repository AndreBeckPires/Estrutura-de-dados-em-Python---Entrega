# Funções para transformação da expressão. De notação infixada para pós-fixada
# Conhecida como Notação Polonesa, é util pois os operadores aparecem antes dos operandos.
# Ideal para representação em uma árvore, simplificando a avaliação da mesma

from operators import OPERATORS

# Separação da expressão em tokens - Números ou Operadores
def tokenize(expressao):
    
    tokens = []
    number = ''
    
    for char in expressao:
        if char.isdigit():
            number += char
        else:
            if number:
                tokens.append(number)
                number = ''
            if char in '()+-*/':
                tokens.append(char)
    if number:
        tokens.append(number)

    return tokens

# Função para converter a expressão infixa para pós-fixa (usando Shunting Yard)
def to_postfix(expressao):

    output = []
    stack = []
    tokens = tokenize(expressao)

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in OPERATORS:
            while (stack and stack[-1] in OPERATORS and
                   OPERATORS[token][0] <= OPERATORS[stack[-1]][0]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('

    while stack:
        output.append(stack.pop())

    return output
