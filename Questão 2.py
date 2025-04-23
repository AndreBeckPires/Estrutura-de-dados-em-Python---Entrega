from classFila import Fila
import random

prioridadeBaixa =  Fila()
prioridadeMedia = Fila()
prioridadeAlta = Fila()
prioridadeIdoso = Fila()

for i in range(0,10):
    paciente = random.randint(1,4)
    match paciente:
        case 1:
            prioridadeBaixa.push(i)
        case 2:
            prioridadeMedia.push(i)
        case 3:
            prioridadeAlta.push(i)
        case 4:
            prioridadeIdoso.push(i)
        case _:
            print("ERROR")


prioridadeBaixa.printFila()
prioridadeMedia.printFila()
prioridadeAlta.printFila()
prioridadeIdoso.printFila()