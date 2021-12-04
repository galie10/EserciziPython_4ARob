n = (int) (input("Inserisci un numero: "))

if(n % 2 == 0):
    print("\nIl numero è divisibile per 2.")
    if(n % 3 == 0):
        print("\nIl numero è divisibile per 3.")
    if(n % 5 == 0):
        print("\nIl numero è divisibile per 5.")
elif n % 3 == 0:
    print("\nIl numero è divisibile per 3.")
    if(n % 5 == 0):
        print("\nIl numero è divisibile per 5.")
elif n % 5 == 0:
    print("\nIl numero è divisibile per 5.")
    if(n % 3 == 0):
        print("\nIl numero è divisibile per 3.")
else:
    print("\nIl numero NON è divisibile per nessuno dei numeri.")