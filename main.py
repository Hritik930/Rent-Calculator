# Inputs We need from the user
# total rent
# Total food ordered for snacking
# charge per unit
# no of person in room

# Output 
# Total amount you've to pay is

rent = int(input ("Enter your hostel/flat rent = "))
food = int(input("Enter the amount spend in food = "))
electricity_spend = int(input("Enter the amount bill in electricity = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons livining in room = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print(f"Each person will pay ₹{output}")










