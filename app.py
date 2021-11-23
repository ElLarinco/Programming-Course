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

numbers = [1,2,3,4,5,6,7]

def plus_numbers(list):
    even = 0
    odd = 0
    for n in list:
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print(f"Pares: {even}")
    print(f"Impares: {odd}")

#plus_numbers(numbers)

def validate(message):
    while True:
        try:
            data = float(input(message))
            return data
        except ValueError:
            print("El data debe ser un número")

def checkZeroDivision(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 / num2

def question():
    largo = validate("Largo en metros: ")
    ancho = validate("Ancho en metros: ")
    m2Xcaja = validate("Metros cuadrados por caja: ")
    precioXm2 = validate("Precio por metro cuadrado: ")

    precioXcaja = (m2Xcaja * precioXm2)
    m2Cuarto = largo * ancho
    #cajas = m2Cuarto / m2Xcaja
    cajas = checkZeroDivision(m2Cuarto, m2Xcaja)
    precioTotal = cajas * precioXcaja

    print(f"Total de cajas que se necesitan {cajas}")
    print(f"Precio total: {precioTotal}")