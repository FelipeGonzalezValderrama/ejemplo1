#funcion 3 parametros
def sumRes(numeros):
    suma = numeros[0] + numeros[1] + numeros[2]
    # inicio variable en cero para asegurar que no falle
    resta = 0
    # recibe una lista de 3 números y devuelve una lista de dos elementos elm1 suma elem2 resta
    if numeros[1] + numeros[2] > numeros[0]:
        resta = numeros[0] - (numeros[1] + numeros[2])
    elif numeros[1] > numeros[0] + numeros[2]:
        resta = numeros[1] - (numeros[0] + numeros[2])
    elif numeros[2] > numeros[0] + numeros[1]:
        resta = numeros[2] - (numeros[0] + numeros[1])
    return [suma, resta]

# Uso: agregamos numeros
numeros = [500, 80, 15]
resultado = sumRes(numeros)
#print resultados fstring
print(f"el resultado de la suma es: {resultado[0]}")
print(f"el resultado de la resta es: {resultado[1]}")


