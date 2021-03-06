import math

def ask():
    while True:
        cords = input("(Введите диапазон от 0 до 999)(Например 20 900)").split()

        if len(cords) == 0 or len(cords)>3:
            print("Введите 2 цифры!!!!(Диапазон от 0 до 999)!!!!")
            continue

        # x-минимальное число дипазона
        # y-максимальное число дипазона
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 998 or 1 > y or y > 999:
            print(" Цифры вне диапазона! ")
            continue

        if x == y:
            print("Два числа не могут быть равны друг другу!!!")
            continue

        if x > y:
            print("Первое число не может быть больше второго!!!")
            continue

        return x, y

#Вводим диапазон
x, y = ask()

def correct(min,max):
    while True:
        numSearch = input(f"Введите угадываемое число с диапазона {min}   {max}")

        if len(numSearch) == 0 or len(numSearch)>3:
            print(f"Введите цифру!!!!(Диапазон от {min} до {max})!!!!")
            continue

        if not (numSearch.isdigit()):
            print(" Введите число! ")
            continue

        num = int(numSearch)

        if num > max or num < min :
            print(" Цифра вне диапазона! ")
            continue

        return num


#Вводим угадываемое число
nSearcn = correct(x,y)


def poisk(n,min,max):
    #Счётчик количества попыток поиска числа
    count = 0
    searchNum = (math.ceil((min + max) / 2))

    while True:
        if searchNum==n:
             count += 1
             break
        elif n<searchNum:
             max = searchNum
             searchNum = (math.ceil((min + max) / 2))
             count += 1
        elif n>searchNum:
             min = searchNum
             searchNum = (math.ceil((min + max) / 2))
             count += 1
    print(f"Я угадал число {n} за {count} попыток.")


poisk(nSearcn,x,y)