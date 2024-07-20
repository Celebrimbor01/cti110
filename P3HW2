 # Dalton Reische
 # 6/30/2024
 # P3HW2
 # Employee pay calculator

#Get employee details
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print('---------------------------------------')

#Calculate pay
regular_hours = min(hours_worked, 40)
overtime_hours = max(hours_worked - 40, 0)
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

#Display pay details
print("Employee Name:", employee_name)
print()
print("Hours Worked     Pay Rate     Overtime     OverTime Pay        RegHour Pay        Gross Pay")
print("---------------------------------------------------------------------------------------------------")
print(f'{hours_worked:<17}{pay_rate:<13}{overtime_hours:<13}{overtime_pay:<20}${regular_pay:<18.2f}${gross_pay:.2f}')
