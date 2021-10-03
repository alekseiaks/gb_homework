data = [1994, True, 'text', ["hello", "world", 1, True], ("hello", "world", 1, True), {"hello", "world", 1, True},
        {"key_1": 1024, 10: 986, "key_3": False, 4: None}, None, b'text']

for i in (data):
    print(f'Элемент списка "{i}" соответствует типу данных: {type(i)}')
