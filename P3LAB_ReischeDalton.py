 # Dalton Reische
 # 6/30/2024
 # P3LAB
 # money calculator
 
user_amount = float(input('Enter the amount of money as a float: $'))

amount_cents = int(user_amount * 100)
    
#Coin values in cents
dollar_value = 100
quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1

#Calculate number of each coin
dollars = amount_cents // dollar_value
amount_cents %= dollar_value
    
quarters = amount_cents // quarter_value
amount_cents %= quarter_value
    
dimes = amount_cents // dime_value
amount_cents %= dime_value
    
nickels = amount_cents // nickel_value
amount_cents %= nickel_value
    
pennies = amount_cents

#Output
if dollars > 0:
    print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
if quarters > 0:
    print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
if dimes > 0:
    print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
if nickels > 0:
    print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
if pennies > 0:
    print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")
if user_amount == 0.00:
    print(f"No change")
