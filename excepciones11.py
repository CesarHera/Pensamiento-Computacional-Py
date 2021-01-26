def run():

    def dividir_lista(lista, divisor):
        try:
            return [i / divisor for i in lista]
        except ZeroDivisionError as e:
            print(f'Error: {e}')        

    lista = range(1, 10)
    divisor = 2

    print(dividir_lista(lista, divisor))

# Excepciones comunes:
# ImportError : una importación falla;
# IndexError : una lista se indexa con un número fuera de rango;
# NameError : se usa una variable desconocida ;
# SyntaxError : el código no se puede analizar correctamente
# TypeError : se llama a una función en un valor de un tipo inapropiado;
# ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado

if __name__ == '__main__':
    run()