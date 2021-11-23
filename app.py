def greet(name):
    return f"Hola {name}"

while True:
    attempts = 0
    ask_name = input("Como te llamas? ('q' para salir): ")
    if ask_name == "q":
        print(f"Número de intentos: {attempts}")
        break
    else:
        print(greet(ask_name))
        attempts += 1

letters = ["a", "b", "c"]
print("Letras:")
for letter in letters:
    print("Letra {}".format(letter))