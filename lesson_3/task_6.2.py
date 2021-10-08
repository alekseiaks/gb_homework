def int_func(text):
    first_letter = text[0].upper()
    text = text.replace(text[0], first_letter, 1)
    return text


text_general = input().split()
last_text = ""
for i in text_general:
    last_text += int_func(i) + " "

print(last_text)
