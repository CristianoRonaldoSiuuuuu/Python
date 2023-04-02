USD_TO_EUR = 0.85
USD_TO_JPY = 109.43

amount = float(input("Enter the amount you want to convert: "))
currency_in = input("Enter the currency you have (USD, EUR, or JPY): ").upper()
currency_out = input("Enter the currency you want to convert to (USD, EUR, or JPY): ").upper()

if currency_in == "USD":
    usd_amount = amount
elif currency_in == "EUR":
    usd_amount = amount / USD_TO_EUR
elif currency_in == "JPY":
    usd_amount = amount / USD_TO_JPY
else:
    print("Invalid input currency.")
    exit()

if currency_out == "USD":
    output_amount = usd_amount
elif currency_out == "EUR":
    output_amount = usd_amount * USD_TO_EUR
elif currency_out == "JPY":
    output_amount = usd_amount * USD_TO_JPY
else:
    print("Invalid output currency.")
    exit()

print(f"{amount:.2f} {currency_in} = {output_amount:.2f} {currency_out}")
