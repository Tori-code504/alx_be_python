monthly_income =int(input("Enter your monthly Income: "))
total_monthly_expenses =int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}" )
print(f"Projected savings after one year, with interst, is: ${projected_savings}")