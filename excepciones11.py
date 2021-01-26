def run():

    def dividir_lista(lista, divisor):
        try:
            return [i / divisor for i in lista]
        except ZeroDivisionError as e:
            print(f'Error: {e}')        

    lista = range(1, 10)
    divisor = 2

    print(dividir_lista(lista, divisor))

if __name__ == '__main__':
    run()