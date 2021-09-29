vyruchka = int(input("Введите значение выручки фирмы: "))
izderzhki = int(input("Введите значение издержек фирмы: "))
prybyl = vyruchka - izderzhki
rentabelnost = prybyl / vyruchka
if prybyl > 0:
    print(f"Фирма отработала  с рентабельностью {rentabelnost}")
    kol_vo__sortud = int(input("Введите численность сотрудников компании: "))
    prybyl_na_odnogo = prybyl / kol_vo__sortud
    print(f"Прибыль на одного сотрудника: {prybyl_na_odnogo}")
else:
    print("Компания отработала в убыток")
