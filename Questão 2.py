from classFila import Fila


prioridadeBaixa =  Fila()
prioridadeMedia = Fila()
prioridadeAlta = Fila()

prioridadeBaixa.push(0)
prioridadeBaixa.push(1)
prioridadeBaixa.push(2)
prioridadeBaixa.push(3)
prioridadeBaixa.printFila()
prioridadeBaixa.pop()
prioridadeBaixa.printFila()
print(prioridadeBaixa.getProximo())