import aproximacion4
import busqueda_binaria5

print("""¡Hola! Te ayudaré a encontrar la raíz cuadrada del número que escribas.
Puedes escoger qué algoritmo voy a usar para que compares su velocidad.
Si deseas detener el proceso de algún algoritmo, presiona las teclas: Ctrl + c
Teclea el número 1 para utilizar el algorítmo de aproximación de soluciones.
Teclea el número 2 para utilizar el algorítmo de enumeración exhaustiva.""")
seleccion = int(input('¿Cuál elijes?: '))

if seleccion == 1:
    aproximacion4.aprox()
elif seleccion == 2:
    busqueda_binaria5.binaria()
else:
    print('Ingrese una opción correcta.')