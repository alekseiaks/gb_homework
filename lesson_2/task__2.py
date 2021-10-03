list = []
number_of_elements = int(input("Сколько элементов должен содержать список? Введите число: "))
for i in range(number_of_elements):
    element = input("Введите значение которое нужно добавить: ")
    list.append(element)
list_1 = []
num_index = 0
for j in list:
    item = list.pop(num_index + 1)
    list.insert(num_index, item)
    num_index += 2
    if num_index >= len(list) - 1:
        break
print(list)
