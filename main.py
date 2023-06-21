import string
import secrets

import unittest


def main():
    length, complexity = get_user_input()
    print(f"Tu contraseña es: {password_generator(length, complexity)}")


def get_user_input():
    levels = {
        1: "Letras",
        2: "Letras y números",
        3: "Letras, números y símbolos",
        4: "Palabras unidas por guiones"
    }
    length = 0
    print("Níveles de complejidad:")
    for level, description in levels.items():
        print(f"{level}. {description}")

    complexity = None
    while complexity not in levels:
        complexity = int(input("Escoger un nível de complejidad de contraseña (1-3): "))
        if complexity == 4:
            length = int(input("Cuantas palabras deseas que tenga tu contraseña, máximo 15: "))
        elif complexity in levels and complexity != 4:
            length = int(input("Ingresar longitud de la contraseña, máximo 100: "))
        if complexity not in levels:
            print(f"{complexity} no es un número válido.")
    return length, complexity


def password_generator(length, complexity):
    password = ""
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 4:
        pass
    else:
        print("Invalid option for complexity")
        return
    for i in range(length):
        password += secrets.choice(characters)
    return password


def get_words(word_count):
    word_list = []
    with open("words_alpha.txt", "r") as file:
        for i in range(word_count):
            word_list.append(secrets.choice(file.readlines()))
    return word_list


class TestPasswordGenerator(unittest.TestCase):
    def test_password_generator_with_letters(self):
        password = password_generator(10, 1)
        self.assertTrue(password.isalpha())
        self.assertTrue(len(password) == 10)

    def test_password_generator_with_letters_and_numbers(self):
        password = password_generator(10, 2)
        self.assertTrue(password.isalnum())
        self.assertTrue(len(password) == 10)

    def test_password_generator_with_letters_and_numbers_and_symbols(self):
        password = password_generator(10, 3)
        self.assertTrue(password.isalnum())
        self.assertTrue(len(password) == 10)


if __name__ == "__main__":
    main()
