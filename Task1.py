import string
from time import sleep
rt = [2,8,10,16]
check = [
    string.digits[:2], string.digits[:8], string.digits, 
    string.ascii_lowercase[:6] + string.ascii_uppercase[:6] + string.digits
    ]
def GetNumSystem():
    while True:
        try:
            numSystem = int(input('Выберите систему исчисления: 2 — двоичная, 8 — восьмиричная, 10 — десятичная, 16 — шестнадцатиричная\n: '))
            if numSystem in rt: return numSystem
            else: print("Введено неверное число.")
        except ValueError: print("Введено не число")

def GetToSystem():
    while True:
        try:
            tonumSystem = int(input('Выберите систему исчисления: 2 — двоичная, 8 — восьмиричная, 10 — десятичная, 16 — шестнадцатиричная\n: '))
            if tonumSystem in rt: return tonumSystem
            else: print("Введено неверное число.")
        except ValueError: return print("Введено не число")

def val(_numSystem):
    value = input('Введите число: ')
    if _numSystem == 2:
        for char in value:
            if char in check[0]:
                pass
            else: 
                print("Двоичное число может содержать только цифры 0-2\n\n")
                sleep(1)
                value = 0
                main()
        pass
        return value
    elif  _numSystem == 8:
        for char in value:
            if char in check[1]:
                pass
            else: 
                print("Восьмиричное число может содержать только цифры 0-7\n\n")
                sleep(1)
                value = 0
                main()
        pass
        return value
    elif _numSystem == 10:
        for char in value:
            if char in check[2]:
                pass
            else: 
                print("Десятичное число может содержать только цифры 0-9\n\n")
                sleep(1)
                value = 0
                main()
        pass
        return value
    elif _numSystem == 16:
        for char in value:
            if char in check[3]:
                pass
            else: 
                print("Шестнадцатиричное число может содержать только цифры 0-9 и буквы A-F\n\n")
                sleep(1)
                value = 0
                main()
        pass
        return value


def Convert(_value, _numSystem, _tonumSystem):
    if _tonumSystem == 2:
        return bin(int(_value, _numSystem))
    elif _tonumSystem == 8:
        return oct(int(_value, _numSystem))
    elif (_tonumSystem == _numSystem):
        return int(_value)
    elif (_tonumSystem == 10):
        return int(_value, _numSystem)
    elif (_tonumSystem == 16):
        return hex(int(_value, _numSystem))

def ex():
        var = input("Ещё одно вычесление? Y/N")
        if (var not in "YyNn"):
            print("Введен неверный символ")
            ex()
        elif (var in "Yy"):
            main()
        elif (var in "Nn"):
            exit()

def main():
    while True:
        print ('Исходная система исчисления')
        numSystem = GetNumSystem()
        print ('Число ')
        value = val(numSystem)
        print ('Система исчисления в которую нужно перевести число')
        tonumSystem = GetToSystem()
        out = Convert(str(value), numSystem, tonumSystem)
        if tonumSystem == 10: 
            print(out)
        else:
            print (out[2:])
        ex()

if __name__ == "__main__":
    main()
