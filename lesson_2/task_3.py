number_of_month = int(input('Enter the month number: '))
if number_of_month in (12, 1, 2):
    print("Winter")
elif number_of_month in (3, 4, 5):
    print("Spring")
elif number_of_month in (6, 7, 8):
    print("Summer")
elif number_of_month in (9, 10, 12):
    print("Fall")
    
