#proframm leiab tehtes x väärtuse, antud avaldise puhul
import cmath
print("Tere! Programm arvutab sulle ruutvõrrandi vastused!")
print("Sisesta a:")
a = int(input())
print("Sisesta b:")
b = int(input())
print("Sisesta c:")
c = int(input())
d =(b**2- 4*a*c)
if  d < 0 :
    print("Lahendid puuduvad")
else:
    x1 = round((-b + d ** (1/2))/2*a)
    x2 = round((-b - d ** (1/2))/2*a)
    print(x1)
    print(x2)