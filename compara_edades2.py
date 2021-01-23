def run():
    nombre1 = input("""🎇 Bienvenido al programa comparador de edades, necesito algunos datos para empezar.
Dime el nombre de la primer persona: """).capitalize()
    edad1 = int(input('Ahora dime su edad: '))
    nombre2 = input('Dime el nombre de la segunda persona: ').capitalize()
    edad2 = int(input('Ahora dime su edad: '))

    if edad1 < edad2:
        print(f'{nombre1} es menor que {nombre2} 🎇')
    elif edad1 > edad2:
        print(f'{nombre1} es mayor que {nombre2} 🎇')
    else:
        print('Son de la misma edad 🎇')

if __name__ == "__main__":
    run()