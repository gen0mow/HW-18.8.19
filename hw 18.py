k = int(input("Введите нужное количество билетов"))
age = []
for a in range(k):
     age.append(int(input(f"Введите возраст посетителя №{a + 1}: ")))
result = 0
for i in range(k):
    if age[i] < 18:
        res = 0
    elif 18 <= age[i] < 25:
        res = 990
    else:
        res = 1390

    result += res
if k > 3:
    result = result*0.9
print(f"Общая стоимость билетов для {k} человек: {round(result)} руб.")