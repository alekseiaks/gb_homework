proverka = 0
while True:
    integer = int(input("Введите целое положительное число: "))
    if integer > 0:
        while integer > 0:
            posl_int = integer % 10
            integer = integer // 10
            if proverka < posl_int:
                proverka = posl_int
        print(proverka)
    else:
        print("Введите  целое и положительное число")
