import time

def countdown(timer):
    while timer > 0:
        min = int(timer/60)
        seg = int(timer%60)
        print(f'{min}:{seg}')
        time.sleep(1)
        timer -= 1

    print("TEMPO ESGOTADO!")

c = int(input("Digite o tempo em segundos: "))
countdown(c)