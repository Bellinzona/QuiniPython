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

def analizarApuesta(a, apuesta,c):
    print()
    
    print("apuesta", apuesta)
    apuestaTotal = 0
    b = str(int(apuesta))
    numerosJugados = len(b)
    multi = 0

    if numerosJugados == 4:
        multi = 3500
    elif numerosJugados == 3:
        multi = 500
    elif numerosJugados == 2:
        multi = 70
    else:
        multi = 7

    

    if a > 10:
        for i in range(10):
            numero = str(matriz[i + 1][1])
            numero = numero[-len(b):]
            print("n", numero)
            
            if int(numero) == int(b):
                print(f"INCREIBLE {numero} ES IGUAL A {apuesta}")
    
                if a == 20:
                    apuestaTotal += (int(c) // a) * multi
                    print("gano $", apuestaTotal)

                if a == 15:
                    apuestaTotal += (int(c) // a) * multi
                    print("gano $", apuestaTotal)
                
    
        for j in range(a - 10):
            numero = str(matriz[j + 1][3])
            numero = numero[-len(b):]
            print("n", numero)
            if int(numero) == int(b):
                print(f"INCREIBLE {numero} ES IGUAL A {apuesta}")

                if a == 20:
                    apuestaTotal += (int(c) // a) * multi
                    print("gano $", apuestaTotal)
                    

                if a == 15:
                    apuestaTotal += (int(c) // a) * multi
                    print("gano $", apuestaTotal)

                

    else:
        for i in range(a):
            numero = str(matriz[i + 1][1])
            numero = numero[-len(b):]
            print("n", numero)
            if int(numero) == int(b):
                print(f"INCREIBLE {numero} ES IGUAL A {apuesta}")
                
                if a == 1:
                    apuestaTotal += (c // a) * multi
                    print("gano", apuestaTotal)
                    
                elif a == 5:
                    apuestaTotal += (c // a) * multi
                    print("gano", apuestaTotal)

try:
    arch = open("quini.txt", "r", encoding="utf-8")
except:
    print("algo salio mal")

for linea in arch:
    partes = linea.split(";")
    Dni = partes[0]
    agencia = partes[1]
    apuesta = partes[2]
    ubicacion = int(partes[3])
    dinero = partes[4]
    analizarApuesta(ubicacion, apuesta,dinero)
