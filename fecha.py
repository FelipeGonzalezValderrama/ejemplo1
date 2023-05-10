from datetime import datetime

now = datetime.now()

aa = now.year
ma = now.month
da = now.day
print(aa, ma, da)

print("bienvenido al programa introduzca sus datos:")

an = int(input("introduzca su año de nacimiento: "))
mn = int(input("introduzca su mes de nacimiento: "))
dn = int(input("introduzca su dia de nacimiento: "))

edad = aa - an - ((ma, da) < (mn, dn))

print(f"Su edad es {edad} años")
