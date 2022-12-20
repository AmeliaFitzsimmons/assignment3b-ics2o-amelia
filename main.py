print("Pizza Price Calculator")
size = input("What size pizza do you want? L or XL: ")
one_topping = input("Do you want 1 topping? Y or N: ")
two_toppings = input("Do you want 2 toppings? Y or N: ")
three_toppings = input("Do you want 3 toppings? Y or N: ")
four_toppings = input("Do you want 4 toppings? Y or N: ")
bill = 0

if size == "L":
    bill += 6
elif size == "XL":
    bill += 10

if one_topping == "Y":
        bill += 1
if two_toppings == "Y":
        bill += 1.75
if three_toppings == "Y":
        bill += 2.50
if four_toppings == "Y":
        bill += 3.35
    
print(f"Your subtotal is {bill}") 

tax = bill*0.13
print(f"Your Tax is {tax}")
print(f"Your final Total is {bill+tax}")