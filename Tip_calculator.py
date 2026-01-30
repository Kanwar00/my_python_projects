print("Welcome to the Tip Calculator")
total_bill=int(input("What is your total bill: $"))

tip=int(input("How much % would you like to tip? "))

no_of_people=int(input("How many people are splitting the bill? "))

final_amount=round((total_bill+(total_bill*tip/100))/no_of_people,2)

print(f"Everyone should pay  ${final_amount}")

