objetivo = int(input('¡Hola! Intentaré encontrar la raíz cuadrada del número que elijas: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta +=1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raíz cuadrada exacta 🙁')