#!usr/bin/env python 3.8

print ("HOla Willson")


#Diferencia entre .py y .pyw
#Los programas Python pueden tener dos extensiones: .py y .pyw. La más utilizada es la primera, .py.

#Si se ejecutan desde IDLE, no hay diferencia entre ambas extensiones.

#Pero si se ejecutan desde un terminal o haciendo doble clic sobre los ficheros, entonces sí que hay diferencias. Los archivos .py son ejecutados por python.exe,
#mientras que los archivos .pyw son ejecutados por pythonw.exe. 
#La principal diferencia es que python.exe crea una ventana de terminal (o aprovecha la ventana de terminal desde la que se ejecuta el programa), 
# ventana que permite pedir valores al usuario o imprimir mensajes, mientras que pythonw.exe no crea ninguna ventana de terminal.

#Solamente se debe utilizar la extensión .pyw si el programa crea y gestiona su propia ventana de interfaz de usuario o si no queremos ni 
# pedir datos al usuario ni mostrarle ninguna salida del programa. En caso contrario, es mejor utilizar la extensión .py.

#Otra diferencia es que python.exe ejecuta los programas de forma síncrona, es decir, que en un terminal no se puede ejecutar un nuevo programa .py 
# hasta que ha terminado el programa anterior, mientras que pythonw.exe ejecuta los programas de forma asíncrona, 
# es decir, que se pueden ir ejecutando nuevos programas aunque los anteriores no hayan terminado de ejecutarse.

