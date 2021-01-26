def run():


    def primeras_palabras(lista_palabras):
        lista_primeras_palabras = []
        for palabra in lista_palabras:
            assert type(palabra) == str, f'{palabra} No es una string 🙁'
            assert len(lista_palabras) > 0, 'No se permiten strings vacías 🤔'

            lista_primeras_palabras.append(palabra[0])
        print(lista_primeras_palabras)


    palabras = ['Tourkey', 'Aroesti', 'Math', 'Cup', 'Phycharm']
    primeras_palabras(palabras)


if __name__ == '__main__':
    run()