# Project Day 2 : Tip Calculator (Beginner)

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
pourcentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
total = (total_bill + total_bill*pourcentage_tip*0.01)/num_people
# round (number, how much after the comma) ex. round(124.9295,2) => 124.93
print("Each person should pay: $", round(total, 2))

