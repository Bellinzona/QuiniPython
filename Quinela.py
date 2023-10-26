import random


def generarNumero():
    numero = random.randint(0, 9999)
    numero_formateado = "%04d" % numero
    return numero_formateado

def generarMatriz():
    matriz = []
    lugar = 0
    for f in range(12):
        matriz.append([])
        for c in range(4):
            matriz[f].append(0)

    matriz[0][0] = "Ubicacion"
    matriz[0][1] = "Numero"
    matriz[0][2] = "Ubicacion"
    matriz[0][3] = "Numero"
    

    for f in range(10):
        lugar += 1
        for c in range(4):
            matriz[f + 1][0] = lugar
            matriz[f + 1][1] = generarNumero()

    for f in range(10):
        lugar += 1
        matriz[f + 1][2] = lugar
        matriz[f + 1][3] = generarNumero()

    for f in range(11):
        for c in range(4):
             print("{:<10}".format(matriz[f][c]), end=" ")
        print()

    return matriz

matriz = generarMatriz()

def analizarApuesta():
    

    for f in range(11):
        for c in range(4):
             print("{:<10}".format(matriz[f][c]), end=" ")
        print()
            



try:
    arch = open("quini.txt","r", encoding="utf-8")
    
except:
    print("algo salio mal")


for linea in arch:
        partes = linea.split(";")

        Dni = partes[0]
        agencia = partes[1]
        apuesta = partes[2]
        ubicacion = partes[3]
        dinero = partes[4]
        
        print(Dni,agencia,apuesta,ubicacion, dinero)


analizarApuesta()
