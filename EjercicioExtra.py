# Copyright 2021 Castillo

import random

# Inicializamos la matriz, las filas y columnas
matriz = []
columnas = 0
filas = 0

# Función para cargar la matriz con números aleatorios del 10 al 99.
def carga(matriz):
    for h in range(filas):
        # Añadimos una matriz para cada una de las columnas 
        matriz.append([] * filas)
        for b in range(columnas):
            matriz[h].append(random.randint(10,99))
        

# Función que ordena la matriz con cuadruples For mediante método Burbuja.
def ordenar(matriz):
    menor =0
    for i in range(filas):
        for j in range(columnas):
            for x in range(filas):
                for y in range(columnas):
                    if (matriz[i][j] < matriz[x][y]):            
                        menor = matriz[i][j]
                        matriz[i][j] = matriz[x][y]
                        matriz[x][y] = menor
                

# Función para mostrar el Array Bidimensional
def mostrar(matriz): 
    for i in range(filas): 
        for j in range(columnas):
            print(str(matriz[i][j])+"|",end="")           
        print("")

# Núcleo del programa con manejo de excepciones
while True:
    try:
        print("CREAREMOS UN MATRIZ BIDIMENSIONAL DE NÚMEROS ALEATORIOS\n")
        columnas = int(input("¿De cuántas columnas? "))
        filas = int(input("¿Y cuantas filas tendrá? "))
        print("CREANDO........")
        carga(matriz)
        mostrar(matriz)
        print("\nY LA ORDENAMOS")
        ordenar(matriz)
        mostrar(matriz)
        print("\nMuchas Gracias por participar")
        exit(2)

    except(ValueError):
        print("No has introducido un número!")
    
    except(KeyboardInterrupt):
        print("\nSaliendo......")
        exit (2)











