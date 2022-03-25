"""Генератор приветствий."""


def greeting():
    name = input("Введите ваше имя: ").title()

    print("Привет,", name)


if __name__ == "__main__":
    greeting()
