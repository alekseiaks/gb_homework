rating = [7, 5, 3, 3, 2]
digit = int(input("Введите число: "))
if rating[0] < digit:
    rating.insert(0, digit)
elif rating[-1] > digit:
    rating.append(digit)
else:
    for i in range(len(rating)):
        if rating[i] > digit:
            continue
        else:
            rating.insert(i + 1, digit)
            break
print(rating)
