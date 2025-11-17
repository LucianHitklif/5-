income = float(input("Годовой доход "))
tax = income * 0.13
income1 = income - tax
print(f"Сумма годового дохода: {income}")
print(f"Сумма расчитанного налога: {tax}")
print(f" Сумма на руки после вычета налога: {round(income1, 2)}")

