def run():
    n = int(input('Teclea un número y te diré a cuál número de Fibonacci pertenece: '))

    def fibonacci(n):
        if n == 0 or n == 1:
            return 1
        
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(fibonacci(n))



if __name__ == '__main__':
    run()