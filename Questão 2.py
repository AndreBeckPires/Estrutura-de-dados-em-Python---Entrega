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
            print(f"Chegada do paciente {i}: Baixa Prioridade")
            prioridadeBaixa.push(i)
        case 2:
            print(f"Chegada do paciente {i}: Media Prioridade")
            prioridadeMedia.push(i)
        case 3:
            print(f"Chegada do paciente {i}: Alta Prioridade")
            prioridadeAlta.push(i)
        case 4:
            print(f"Chegada do paciente {i}: Idoso Prioridade")
            prioridadeIdoso.push(i)
        case _:
            print("ERROR")


atendimentos = (prioridadeBaixa.getSize() + prioridadeMedia.getSize() + prioridadeAlta.getSize() + prioridadeIdoso.getSize())
prioridadeBaixa.printFila()
prioridadeMedia.printFila()
prioridadeAlta.printFila()
prioridadeIdoso.printFila()
while atendimentos > 0:
    if prioridadeIdoso.getSize() > 0:
        print(f"Atendendo paciente {prioridadeIdoso.getProximo()}")
        prioridadeIdoso.pop()
    elif prioridadeAlta.getSize() > 0:
        print(f"Atendendo paciente {prioridadeAlta.getProximo()}")
        prioridadeAlta.pop()
    elif prioridadeMedia.getSize() > 0:
        print(f"Atendendo paciente {prioridadeMedia.getProximo()}")
        prioridadeMedia.pop()
    elif prioridadeBaixa.getSize() > 0:
        print(f"Atendendo paciente {prioridadeBaixa.getProximo()}")
        prioridadeBaixa.pop()
    atendimentos -= 1

print("Atendimentos finalizados!")

#O(n) -> Onde N são 10 