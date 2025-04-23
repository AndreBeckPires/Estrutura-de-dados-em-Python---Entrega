class Fila():
    def __init__(self):
        self.objetos = []

    def push(self,obj):
        self.objetos.append(obj)
    
    def getSize(self):
        return len(self.objetos)
    
    def pop(self):
        self.objetos.pop()

    def printFila(self):
        print(self.objetos)

    
