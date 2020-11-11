

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal 
#y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el 
# índice de masa corporal calculado redondeado con dos decimales.


# Para calcular el índice de masa corporal la regla sería = PESO / (ESTATURA * ESTATURA)
while True:
    try:
        peso= float(input("Introduce tu peso: "))
        estatura = float(input("Introduce tu estatura: "))
        imc= round(peso / (estatura*estatura))
        print("Tu IMC es de {}.".format(imc))
        break
    except ValueError:
        print("El valor introducido no es válido")


"""
Según la SEEDO (Sociedad Española para el Estudio de la Obesidad) estos son los tipos de resultados según el IMC obtenido:

+Bajo peso: por debajo de 18.5
+Peso normal o «normopeso»: entre 18.5-24.9
+Sobrepeso: entre 25.0-29.9
+Obesidad: por encima de 30
+Obesidad mórbida o severa: mayor de 40

"""