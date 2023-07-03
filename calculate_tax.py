# Calculate income tax for the given income by adhering to the below rules.


total_income = int(input("Total Income: "))
taxable_income = 10000*0 + 10000*(1/10) + (total_income-20000)*(2/10)


print(f"Taxable Income: {taxable_income}")


