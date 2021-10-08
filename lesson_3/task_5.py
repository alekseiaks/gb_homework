def summ_1(digits):
    summ = 0
    while True:
        digits = digits.split()
        if len(digits) == 1 and digits[0].lower() == 'e':
            print("Вы закончили проasграмму. ")
            break
        for j in digits:
            if j.isdigit() == False and digits[len(digits) - 1].lower() != "e":
                print("Неправильный ввод, попробуйте снова!")
                digits = input("Введите числа через пробел, для того чтобы закончить программу введите 'e': ").split()
        if digits[-1].lower() == "e":
            del digits[len(digits) - 1]
            for i in digits:
                summ += int(i)
            print(summ)
            print("Вы закончили программу. ")
            break
        else:
            for i in digits:
                summ += int(i)
            print(summ)
            digits = input("Введите числа через пробел, для того чтобы закончить программу введите 'e': ")


digits = input("Введите числа через пробел, для того чтобы закончить программу введите 'e': ")
summ_1(digits)
