def get_byte_representation(character):
    return format(ord(character), '08b')

def byte_representation_of_character():
    char = input("Ingrese un carácter: ")
    byte_repr = get_byte_representation(char)
    print(f"La representación en byte de '{char}' es: {byte_repr}")

def byte_representation_of_word():
    word = input("Ingrese una palabra: ")
    byte_repr = ' '.join([get_byte_representation(char) for char in word])
    print(f"La representación en byte de '{word}' es: {byte_repr}")

def main():
    menu=0
    while menu !=3:
        menu = int(input("Menú\n=====\n1. Generar representación en byte de un carácter\n2. Generar representación en byte de una palabra\n3. Salir\nSeleccione una opción: "))

        if menu == 1:
            byte_representation_of_character()
        elif menu == 2:
            byte_representation_of_word()
        elif menu == 3:
            print("¡Hasta luego!")
         
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
main()
