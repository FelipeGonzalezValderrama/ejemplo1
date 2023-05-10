"""Imprime los números desde el 1 al 19. Saltando el número ingresado
previamente por el usuario."""
#ingresa numero por consola para que no aparezca
sacaNumero = int(input("lanzate un numero del 1 al 19 para que no aparezca=> "))
#ciclo para recorrer 
for i in range(1, 20):
    #si es igual al numero ingresado en consola saca numero y ciclo termina
    if i != sacaNumero:
        print(f"{i}-- ",end="")


