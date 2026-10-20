# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading

if name.strip() == "":
  print("Invalid name. Try again please.")
  name = input("Enter customer name: ")
  
  if previous.isdigit() or not (0 >= float(previous)):
    print("Invalid reading. Put valid previous meter reading.")
    previous = float(input("Enter previous meter reading: "))
    
if current.isdigit() or not (0 >= float(current) >= previous):
      print("Invalid reading. Enter current meter reading again.")
      current = float(input("Enter current meter reeading: "))
