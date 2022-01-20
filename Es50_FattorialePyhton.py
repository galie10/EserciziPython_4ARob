def fattoriale(num):
    if num==0:
        return 1
    else:
        return num*fattoriale(num-1)

def main():
    n = int(input("Inserisci il numero: "))
    print ("Il fattoriale del numero scelto è", fattoriale(n))

if __name__ == "__main__":
    main()