 # Dalton Reische
 # 6/15/2024
 # P1HW2
 # Travel expense calculator
print('This program calculates and displays travel expenses', end=' ')
print()
print()
# User enters their budget
user_budget = float(input('Enter budget: '))
print()
# User enters their destination
user_destination = input('Enter your travel destination: ')
print()
# User enters their expected gas cost
user_gas = float(input('How much do you think you will spend on gas? '))
print()
# User enters their expected accomodation cost
user_hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
# User enters their expected food cost
user_food = float(input('Last, how much do you need for food? '))
print()
# Displays everything the user inputed back to them
print('------------Travel Expenses------------')
print('Location: ', user_destination)
print('Initial Budget: ', user_budget)
print()
print('Fuel: ', user_gas)
print('Accomodation: ', user_hotel)
print('Food: ', user_food)
# Calculates the users expenses and subtracts it from their budget
user_expenses = user_gas + user_hotel + user_food
remaining_balance = user_budget - user_expenses
print()
# Displays the users left over balance
print('Remaining Balance: ', remaining_balance)
