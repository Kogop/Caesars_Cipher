# import random


# def Shifr(str):
#   ran = random.randint(0, 33)
#   print(ran)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#   print("Введите предложение для зашифровки")
#   c = input()
#  print(c)
#  Shifr(c)


alfavit_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

itog = ''
if __name__ == '__main__':
    smeshenie = int(input('Шаг шифровки: '))
    message_to_shipr = input("Сообщение для шифровки: ").lower()

    for i in message_to_shipr:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
        if new_mesto > 33:
            new_mesto -=33
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i

print(itog)
