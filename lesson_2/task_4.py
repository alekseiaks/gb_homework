words = input("Введите слова через пробел: ")
list_words = words.split()
for i in list_words:
    if len(i) >= 10:
        print(i[:10])
    else:
        print(i)
