import random
lanciA = [random.randrange(1, 7, 1) for k in range(1,11) if random.randrange(1, 7, 1) < 7]
lanciB = [random.randrange(1, 7, 1) for k in range(1,11) if random.randrange(1, 7, 1) < 7]

k = 0
f = open(".\lanciodadi.txt", "w")

while(k < 10):
    f.write(f"{lanciA[k]}, ")
    f.write(f" {lanciB[k]}")
    f.write("\n")
    k+=1
