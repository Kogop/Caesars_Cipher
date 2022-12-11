import re
alfavit_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

itog = ''
if __name__ == '__main__':
    smeshenie = int(input('Шаг шифровки: '))
    message_to_shipr = input("Сообщение для шифровки: ").lower()

    for i in message_to_shipr:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
        while new_mesto > 32:
            new_mesto -= 32
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
print("Zawivrovannoe message ->", itog)
TempItog = '%s' % itog
check = 0
for t in range(1, 32):
    f = open('russian.txt', 'r')
    first_word = next(m.group() for m in re.finditer(r'\w+', itog))
    for line in f.readlines():
        if re.match(first_word, line, re.I):
            #print(line)
            check = 1
            break

    if check == 0:

        itog = ''
        for i in TempItog:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto - t
            if new_mesto < 0:
                new_mesto += 32
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
        print(itog)
    else:
        print("\n Raswifrovanniy Otwet --> ", itog)
        break

    f.close()
