class Nodo:
    def __init__(self, valor, isFolder, isFile):
        self.valor = valor
        self.childrens = []
        self.parent = None
        self.isFolder = isFolder
        self.isFile = isFile

    def setParent(self, nodo):
        self.parent = nodo

    def setChildren(self,nodo):
        if(self.isFolder):
            self.childrens.append(nodo)
            self.childrens[(len(self.childrens)-1)].setParent(self)


    
    def getValue(self):
        return self.valor
    
    def getParent(self):
        return self.parent.getValue()
    
    def getChildrens(self):
        return self.childrens


