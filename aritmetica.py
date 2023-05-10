#definir funciones aritmeticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

#definir operaciones
def operaciones(a, b):
    suma = sumar(a, b)
    resta = restar(a, b)
    multiplicacion = multiplicar(a, b)
    division = dividir(a, b)

    resultado = {
        "Suma": suma,
        "Resta": resta,
        "Multiplicacion": multiplicacion,
        "Division": division
    }

    return resultado
