USD_TO_RUB = 95.50
def convert_usd_to_rub(amount_usd):
    return round(amount_usd * USD_TO_RUB)
usd = float(input("Сумма в долларах: "))
rub = convert_usd_to_rub(usd)
print(f"{usd} USD = {rub} RUB")