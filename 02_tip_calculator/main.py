#Write your code below this line 👇
print("Welcome to the tip calc")
bill = float(input("What is the total bill? $ "))
tip = int(input("Percentage tip? 10/12/20 "))
count_clients = int(input("How many people to split the bill? "))

percent  = 1 + tip/100
part = round(bill * percent / count_clients, 2)

print("Each person should pay: $"+"%.2f"%part)

# print(f"Each person should pay: ${part}")