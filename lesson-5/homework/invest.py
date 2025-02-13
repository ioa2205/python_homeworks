def invest(amount, rate, year):
    for i in range(year):
        amount = amount*(1 + rate)
        print(f"year {i+1}: {round(amount,2)}")
amount = float(input("Enter an initial amount: "))
rate = float(input("Enter an annual percentage rate: "))
year = int(input("Enter the number of years: "))
invest(amount, rate, year)