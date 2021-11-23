import math

def greet(name):
    return f"Hola {name}"

def loop ():
    while True:
        attempts = 0
        ask_name = input("Como te llamas? ('q' para salir): ")
        if ask_name == "q":
            print(f"Número de intentos: {attempts}")
            break
        else:
            print(greet(ask_name))
            attempts += 1

def array():
    letters = ["a", "b", "c"]
    print("Letras:")
    for letter in letters:
        print("Letra {}".format(letter))

def pseudocode1():
    numbers = []

    A = float(input("Num A: "))
    numbers.append(A)

    B = float(input("Num B: "))
    numbers.append(B)

    C = float(input("Num C: "))
    numbers.append(C)

    if (A == B or B == C or C == A or B == C):
        print("No se permiten valores iguales")
    else:
        print(f"Mayor: {max(numbers)}")
        print(f"Menor: {min(numbers)}")

#pseudocode1()

def pseudocode2(n1, n2):
    H = math.sqrt(pow(n1, 2) + pow(n2, 2))
    print(H)

#pseudocode2(2, 4)

def pseudocode3(radio, height):
    Area = (2 * (math.pi) * radio * height) + (2 * (math.pi) * pow(radio, 2))
    Volume = math.pi * (pow(radio, 2) * height)
    print(f"Area: {Area}")
    print(f"Volumen: {Volume}")

#pseudocode3(2, 4)