def my_func(x, y):
    for i in range(y - 1):
        x *= x
    return x

print(my_func(5,3))