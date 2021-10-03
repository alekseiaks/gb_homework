goods = {}
keys = ["Наименование", "Цена", "Количество", "Ед."]
text = ["Введите наименование товара: ", "Введите цену товара за 1 единицу: ", "Введите количество товара, имеющегося "
                                                                               "на складе: ",
        "Введите единицу измерения товара(например - шт.): "]
list_and_numbers = []  # список для создания кортежа (1, {словарь}])
names_variables = []  # список для имен переменных которые будут созданы
list_number_of_goods = []
quantity_of_goods = int(input("Введите количество различных единиц на складе: "))


for number in range(quantity_of_goods):
    goods = "goods_" + str(number)  # создаем имя переменной для товара
    locals()[goods] = {}  # создаем переменную для товара
    list_number_of_goods.append(number + 1)
    name_variable = 'values_' + str(number)  # создаем имя переменной для
    names_variables.append(name_variable)
    locals()[name_variable] = []

    for j in range(4):
        if j == 1 or j == 2:
            locals()[name_variable].append(int(input(text[j])))
        elif j == 0 or j == 3:
            locals()[name_variable].append(input(text[j]))
    count = 0

    for i in keys:  # создаем словарь
        locals()[goods][keys[count]] = locals()[name_variable][count]
        count += 1

    name_list_and_numbers = "name_list_and_numbers_" + str(number + 1)
    locals()[name_list_and_numbers] = []  # создаем список
    locals()[name_list_and_numbers].append(number + 1)  # добавляем порядковый номер товара
    locals()[name_list_and_numbers].append(locals()[goods])  # добавляем словарь в список
    locals()[name_list_and_numbers] = tuple(locals()[name_list_and_numbers])  # список переводим в кортеж

for number in range(quantity_of_goods):
    print(locals()["name_list_and_numbers_" + str(number + 1)])

names = []
price = []
amount = []
unit = []
dictionary_last = {}
list_names = [names, price, amount, unit]


for number in range(quantity_of_goods):
    names.append(locals()["name_list_and_numbers_" + str(number + 1)][1].get("Наименование"))
    price.append(locals()["name_list_and_numbers_" + str(number + 1)][1].get("Цена"))
    amount.append(locals()["name_list_and_numbers_" + str(number + 1)][1].get("Количество"))
    unit.append(locals()["name_list_and_numbers_" + str(number + 1)][1].get("Ед."))

new_list_unit = []


for un in unit:  # удаляем из списка единиц измерений повторяющися значения.
    if not un in new_list_unit:
        new_list_unit.append((un))

list_dict = [names, price, amount, new_list_unit]
count_2 = 0

dictionary_last = {
    keys[0]: names,
    keys[1]: price,
    keys[2]: amount,
    keys[3]: new_list_unit
}
print(dictionary_last)
