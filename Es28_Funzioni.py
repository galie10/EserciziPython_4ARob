def somma_moltiplicazione(x,y):
    somma = x+y
    prodotto = x*y
    return {"somma":somma,"moltiplicazione":prodotto}

#lambda function
somma_moltiplicazione = lambda x,y : {x+y, x*y}

a = 10
b = 4

print(somma_moltiplicazione(a,b))


