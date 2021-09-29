seconds = int(input("Какое количество секунд перевести в формат времени - чч:мм:сс? "))
hh = seconds // 3600
mm = (seconds - hh * 3600) // 60
ss = seconds - mm * 60 - hh * 3600

print(f"{hh:02d}:{mm:02d}:{ss:02d}")
