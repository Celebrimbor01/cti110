 # Dalton Reische
 # 6/15/2024
 # P1HW1
 # Calculating Exponents, Addition and Subtraction
print('-----Calculating Exponents----', end=' ')
print()
print()
print()
user_value = int(input('Enter an integer as the base value:'))
user_exponent = int(input('Enter an integer as the exponent:'))
exponent = user_value ** user_exponent
print()
print()
print(user_value, 'raised to the power of', user_exponent, 'is',exponent, '!!')
print()
print()
print('-----Addition and Subtraction----')
print()
print()
user_start = int(input('Enter a starting integer:'))
user_add = int(input('Enter an integer to add:'))
user_subtract = int(input('Enter an integer to subtract:'))
add_sub = user_start + user_add - user_subtract
print()
print()
print(user_start, '+', user_add, '-', user_subtract, 'is equal to', add_sub)
