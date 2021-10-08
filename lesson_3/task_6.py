def int_func(text):
    first_letter = text[0].upper()
    text = text.replace(text[0], first_letter, 1)
    return text


print(int_func(input("Введите текст прописными буквами: ")))

