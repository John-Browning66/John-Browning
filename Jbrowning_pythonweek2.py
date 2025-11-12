# Daily Budget Tracker

print("Welcome to Daily Budget Tracker")

daily_budget = float(input("Enter your daily budget: $"))
total_spent = 0.0
continue_tracking = "yes"

while continue_tracking.lower() == "yes":
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input(f"How much did you spend on {expense_name}? $"))
    
    total_spent += expense_amount
    remaining = daily_budget - total_spent
    
    print(f"You have ${remaining:.2f} left.")
    
    if remaining <= 0:
        print("You have reached your budget limit!")
        break
    
    continue_tracking = input("Do you want to add another expense? (yes/no): ")

print(f"Total spent today: ${total_spent:.2f}")
print(f"Remaining budget: ${max(0, remaining):.2f}")
