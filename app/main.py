"""Генератор приветствий."""


def Greeting():
    name = input("Введите ваше имя: ").title()

    print("Привет,", name)


if __name__ == "__main__":
    Greeting()
