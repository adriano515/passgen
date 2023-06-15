def main():
    user_input()


def user_input():
    levels = {
        1: "Letras",
        2: "Números",
        3: "Símbolos"
    }
    length = int(input("Ingresar longitud de la contraseña: "))
    print("Níveles de complejidad:")
    for level, description in levels.items():
        print(f"{level}. {description}")

    complexity = None
    while complexity not in levels:
        complexity = int(input("Escoger un nível de complejidad de contraseña (1-3): "))
        if complexity not in levels:
            print(f"{complexity} no es un número válido.")


if __name__ == "__main__":
    main()