class Pila(): #object è il genitore di tutti i programmi in python
     def __init__ (self):
         self.pila = []
    
     def push(self,elemento):
        self.pila.append(elemento)
     
     def pop(self):
         if(len(self.pila) == 0):
             return None
         else: return self.pila.pop()
    
     def print(self):
         print(self.pila)       #pass per far comunque funzionare il codice anche se non vi è nulla all'interno della funzione

p1 = Pila() #istanza della classe
p1.push("ciao")
p1.push("buongiorno")
p1.print()
