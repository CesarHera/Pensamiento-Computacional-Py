def aprox():
    
    objetivo = int(input('¡Hola! Intentaré encontrar la raíz cuadrada del número que escribas: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta, respuesta**2 - objetivo)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'{objetivo} No tiene raíz cuadrada 🙁')
    else:
        print(f'La raíz cuadradda de {objetivo} es {respuesta}')

if __name__ == "__main__":
    aprox()