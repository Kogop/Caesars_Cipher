import random


def Shifr(str):
    ran = random.randint(0, 33)
    print(ran)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Введите предложение для зашифровки")
    c = input()
    print(c)
    Shifr(c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
