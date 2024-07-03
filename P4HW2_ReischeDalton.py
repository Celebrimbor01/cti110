 # Dalton Reische
 # 7/3/2024
 # P4HW2
 # Employee pay calculator loop

# Variables to store totals
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
num_employees = 0

while True:
    # Get employee details
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
    if employee_name.lower() == 'done':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    #Calculate pay
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Accumulate totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    num_employees += 1
    
    #Display pay details
    print()
    print("Employee Name:", employee_name)
    print()
    print("Hours Worked     Pay Rate     Overtime     OverTime Pay        RegHour Pay        Gross Pay")
    print("---------------------------------------------------------------------------------------------------")
    print(f'{hours_worked:<17}{pay_rate:<13}{overtime_hours:<13}{overtime_pay:<20}${regular_pay:<18.2f}${gross_pay:.2f}')
    print()

# Display results
print("---------------------------------------------")
print("Total number of employees entered:", num_employees)
print("Total overtime pay:", "${:.2f}".format(total_overtime_pay))
print("Total regular pay:", "${:.2f}".format(total_regular_pay))
print("Total gross pay:", "${:.2f}".format(total_gross_pay))
print("---------------------------------------------")

