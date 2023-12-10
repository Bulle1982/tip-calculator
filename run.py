print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip_num = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_persons = int(input("How many people to split the bill?"))

tip_prc = tip_num / 100
tip = bill * tip_prc
total_bill = bill + tip
bill_per_person = round(total_bill / number_of_persons, 2)
print(f"Each person should pay: ${bill_per_person}")


