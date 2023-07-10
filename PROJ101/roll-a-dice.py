import random

question = 'y'

while question == 'y':
   

    n = random.randint(1,6)
    if n == 1:
        print()
        print("[   ]")
        print("[ o ]")
        print("[   ]")
        print()
    elif n == 2:
        print()
        print("[o  ]")
        print("[   ]")
        print("[  o]")
        print()
    elif n == 3:
        print()
        print("[o  ]")
        print("[ o ]")
        print("[  o]")
        print()
    elif n == 4:
        print()
        print("[o o]")
        print("[   ]")
        print("[o o]")
        print()
    elif n == 5:
        print()
        print("[o o]")
        print("[ o ]")
        print("[o o]")
        print()
    elif n == 6:
        print()
        print("[o o]")
        print("[o o]")
        print("[o o]")
        print()

    question = input("Voce quer jogar Y/N?")
    print('\n')
