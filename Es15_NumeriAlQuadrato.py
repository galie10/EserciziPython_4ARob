num1= input("Dammi il primo numero ")
num2= input("Dammi il secondo numero ")

x=[]
num1=float(num1)
num2=float(num2)

x.append(num1**2 + num2**2)
x.append((num1+ num2)**2)
x.append(num1**2 - num2**2)
x.append((num1-num2)**2)

print(x)