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
    apuestaTotal = 0
    b = str(int(apuesta))
    numerosJugados = len(b)
    multi = 0
    ganador = False
    

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
            
            
            if int(numero) == int(b):
                
                ganador = True
    
                if a == 20:
                    apuestaTotal += (int(c) // a) * multi
                    

                if a == 15:
                    apuestaTotal += (int(c) // a) * multi
                    
                
    
        for j in range(a - 10):
            numero = str(matriz[j + 1][3])
            numero = numero[-len(b):]
            
            if int(numero) == int(b):
                
                ganador = True
                if a == 20:
                    apuestaTotal += (int(c) // a) * multi
                    
                    

                if a == 15:
                    apuestaTotal += (int(c) // a) * multi
                    

                

    else:
        for i in range(a):
            numero = str(matriz[i + 1][1])
            numero = numero[-len(b):]
            
            if int(numero) == int(b):
                ganador = True
                
                
                if a == 1:
                    apuestaTotal += (int(c) // a) * multi
                    
                    
                elif a == 5:
                    apuestaTotal += (int(c) // a) * multi
                    
    
    return apuestaTotal,ganador





dniGanadores = []
agenciaGanadores = []
premioGanadores = []
apuestaGanadores = []
numeroGanadores = []
ubicacionGanadores = []
totalTodo = 0
contador = 0
listado = []


try:
    arch = open("apuestasquiniela2.txt", "r", encoding="utf-8")
except:
    print("algo salio mal")



for linea in arch:
    partes = linea.split(";")
    Dni = partes[0]
    agencia = partes[1]
    apuesta = partes[2]
    ubicacion = int(partes[3])
    dinero = partes[4]
    
    total,ganador = analizarApuesta(ubicacion, apuesta,dinero)
    totalTodo += total

    if ganador:
        contador += 1
        dniGanadores.append(Dni)
        agenciaGanadores.append(agencia)
        premioGanadores.append(total)
        apuestaGanadores.append(int(dinero))
        numeroGanadores.append(apuesta)
        ubicacionGanadores.append(ubicacion)


print(f"premios total a pagar: {totalTodo}")
print(f"premio promedio: {totalTodo // contador}")





for f in range(len(premioGanadores) + 1):
    listado.append([])
    for c in range(6):
        listado[f].append(0)


listado[0][0] = "DNI"
listado[0][1] = "Agencia"
listado[0][2] = "Premio"
listado[0][3] = "Apuesta $"
listado[0][4] = "N Apostado"
listado[0][5] = "Ubicacion"

for i in range(len(premioGanadores)):

    listado[i + 1][0] = dniGanadores[i]
    listado[i + 1][1] = agenciaGanadores[i]
    listado[i + 1][2] = premioGanadores[i]
    listado[i + 1][3]= apuestaGanadores[i]
    listado[i + 1][4] = numeroGanadores[i]
    listado[i + 1][5] = ubicacionGanadores[i]




for f in range(len(premioGanadores) + 1):
    for c in range(6):
        print("{:<10}".format(listado[f][c]), end=" ")
    print()

print()
print(f"premios total a pagar: {totalTodo}")
print(f"premio promedio: {totalTodo // contador}")