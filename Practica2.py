alumnos = []
pares=[]
impares=[]
factorial=[]
primos=[]
contador = 0

def factorial(numero): 
    resultado = 1
    x = 1
    while x <= numero:
        resultado = resultado * x
        x = x + 1
    return resultado


def primo(num):
    if num < 1:
        return False
    elif num == 2:
        primos.append(num)
    else:
        for k in range(2, num):
            if num % k == 0:
                return False
        
        primos.append(num)
   
while True:
    try:
        while contador < 25:
            entrada=int(input("introduce la edad de un alumno: "))
            alumnos.append(entrada)
            contador+=1

        for i in alumnos:
            primo(i)
            if i % 2==0:
                pares.append(i)
            else:
                impares.append(i)
        break
        
    except(ValueError):
        print("No has introducido un número!")
    
    except(KeyboardInterrupt):
        print("\nSaliendo......")
        exit (2)


alumnos.sort()
menor=alumnos[0]
mayor=alumnos[-1]

print("La edad de todos los alumnos son: {} ".format(alumnos))
print("Las edades pares son: {} ".format(pares))
print("Las edades impares son: {} ".format(impares))
print("El mayor tiene: {} ".format(mayor))
print("El menor tiene: {} ".format(menor))
print("Las edades que son números primos: {} ".format(primos))

primos.sort()
facto = factorial(primos[-1])
print("El Factorial de {} es : {}".format(primos[-1], facto))
