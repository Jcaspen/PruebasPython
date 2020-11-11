



nombre=input("Introduce tu nombre: ")

while True:
    try:
        repeticiones=int(input("Introduce la cantidad de veces que quieres que se repita tu nombre:  "))
        break
    except:
        print("No has introducido un entero")

print((nombre+"\n") * repeticiones)
