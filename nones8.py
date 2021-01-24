def run():
    for i in range(1, 101, 2):
        if i == 99:
            print(i, end='.')
            break
        print(i, end=', ')

if __name__ == '__main__':
    run()