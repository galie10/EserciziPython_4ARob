class Node:
    def __init__(self,value):
        self.value = value
        self.left = None #istanza nodo sinistro
        self.right = None #istanza nodo destro

    def printNode(self):
        print(self.value)
    
    def insertNode(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else: self.left.insertNode(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else: self.right.insertNode(value)
        else: self.value = value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()
    
    def calcDepth(self):
        contatore = 0
        if self.left:
            self.left.calcDepth()
            contatore+=1
        elif self.right: 
            self.right.calcDepth()
            contatore+=1
        
        return contatore

    def searchNode(self,value):
        if value > self.value:
            valore = value
        elif value > self.right:
            
def main():
    Albero = Node(60)
    Albero.insertNode(34)
    Albero.insertNode(50)
    Albero.insertNode(60)
    Albero.insertNode(36)
    Albero.insertNode(70)
    Albero.insertNode(55)
    Albero.insertNode(23)
    Albero.printTree()
    n = Albero.calcDepth()
    print(n)

if __name__ == "__main__":
    main()
