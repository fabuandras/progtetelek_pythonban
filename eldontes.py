# i: int = int(0)
# i: int = int(0)
# while (n<=0):
#     n = int(input("N= "))
#     osszeg: int = int(0)
# for i in range(0, n + 1):
#     osszeg += i
# print(f"Az első {n} db természetes szám összege: {osszeg}")
import math

n = int(input("\nSzám: "))
prim = True
if n < 2:
    prim = False
else:
    i = 2
    while (i <= math.sqrt(n)) and n % i != 0:
        i += 1
    prim = i > math.sqrt(n)
if prim == True:
    print("Prím")
else:
    print("Nem prím")
