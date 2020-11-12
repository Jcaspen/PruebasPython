# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.



while True:
    try:
        a=0
        e=0
        y=0
        o=0
        u=0

        palabra = input("Introduce una palabra: ")

        for i in palabra:
            if (i=="a"):
                a+=1
            elif (i=="e"):
                e+=1
            elif (i=="i"):
                y+=1
            elif (i=="o"):
                o+=1
            elif (i=="u"):
                u+=1

        print("Contiene {} A, {} E, {} I, {} O y {} U.".format(a,e,y,o,u))
        break

    except:
        print("No introduciste una palabra!")