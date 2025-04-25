import operator

# Define em dicionários os operadores suportados, com a sua respectiva precedência
OPERATORS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
}