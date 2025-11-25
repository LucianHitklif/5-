money = [5000, 2000, 1000, 500, 200, 100]
cash = int(input("Введите сумму для снятия (кратную 100): "))
print("Выдача: ")
for mon in money:
    count = cash // mon
    if count > 0:
        print(f"{mon} руб. - {count} шт.")
        cash -= count * mon

if cash % 100 != 0:
    print("Ошибка: сумма должна быть кратной 100!")