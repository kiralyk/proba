a = int(input("add meg a számot"))
if a % 3 == 0:
    print("oszthaó hárommal")
else:
    print("nem osztható")
r = int(input("add meg a sugarat"))
k = 2*r*3.14
t = (r*r)*3.14
if r > 0:
    print(f"terület:{t},kerület:{k}")


x = int(input("eslö szám"))
y = int(input("eslö szám"))
z = int(input("eslö szám"))
if x+y>z and y+z>x and x+z>y:
    print("A háromszög szerkeszthető")
else:
    print("A háromszög nem szerkeszthető")
