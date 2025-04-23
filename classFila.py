class Fila():
    def __init__(self):
        self.objetos = []

    def push(self,obj):
        self.objetos.insert(0,obj)
    
    def getSize(self):
        return len(self.objetos)
    
    def pop(self):
        self.objetos.pop()

    def printFila(self):
        print(self.objetos)

    def getProximo(self):
        return self.objetos[len(self.objetos)-1]

    
