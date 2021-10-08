def my_func(a, b, c):
    my_list = [a, b, c]
    last_digit = 0
    pre_last_digit = 0
    for i in my_list:
        if pre_last_digit < i:
            pre_last_digit = i
        if last_digit < pre_last_digit:
            last_digit, pre_last_digit = pre_last_digit, last_digit
    return pre_last_digit + last_digit


print(my_func(2, 3, 1))
