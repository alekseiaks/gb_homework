def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


dividend, divider = int(input("Введите делимое: ")), int(input("Введите делитель: "))
print(division(dividend, divider))
