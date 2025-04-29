class Nodo:
    def __init__(self, valor, isFolder, isFile):
        self.valor = valor
        self.childrens = []
        self.parent = None
        self.isFolder = isFolder
        self.isFile = isFile

    def set_parent(self, nodo):
        self.parent = nodo

    def set_children(self,nodo):
        if(self.isFolder):
            self.childrens.append(nodo)
            self.childrens[(len(self.childrens)-1)].set_parent(self)


    
    def get_value(self):
        return self.valor
    
    def get_parents(self):
        return self.parent.get_value()
    
    def get_childrens(self):
        return self.childrens


