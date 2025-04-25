from operators import OPERATORS
from infix import to_postfix

#Arvore Binária - com construtor habilitado para receber os filhos - com print estiloso
class BTree:
    def __init__(self, node, left=None, right=None):
        self.nodeValue = node
        self.left = left
        self.right = right
    
    def _str_helper(self, prefix="", is_left=True):
        result = ""
        if self.right:
            result += self.right._str_helper(prefix + ("│   " if is_left else "    "), False)
        result += prefix + ("└── " if is_left else "┌── ") + str(self.nodeValue) + "\n"
        if self.left:
            result += self.left._str_helper(prefix + ("    " if is_left else "│   "), True)
        return result
    
    def __str__(self):
        return self._str_helper()

# Função para construir a árvore a partir da notação pós-fixa
def generate_expression_tree(postfix_tokens):
    stack = []

    for token in postfix_tokens:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            stack.append(BTree(token, left, right))
        else:
            stack.append(BTree(token))

    return stack[0]

# Avaliação da árvore
def evaluate_tree(node):
    if node.nodeValue in OPERATORS:
        left_val = evaluate_tree(node.left)
        right_val = evaluate_tree(node.right)
        return OPERATORS[node.nodeValue][1](left_val, right_val)
    else:
        return int(node.nodeValue)

########################################################################################
# Avaliador de expressões 

expressao = "((18+12)*(15-5))/3"
#expressao = "((5+4)*(8-3))/3"
print(f"Expressão Avaliada: {expressao}")

expressao_postfix = to_postfix(expressao)
print(f"Expressão PosFixada: {expressao_postfix}")

arvore_expressao = generate_expression_tree(expressao_postfix)
print(f"Árvore da expressão:\n{arvore_expressao}")

resultado = evaluate_tree(arvore_expressao)
print(f"Resultado da expressão: {resultado}")