print("Welcome to Python Pizza Deliveries !!!")
size = input("What size pizza do you want? S, M or L:").upper()
pepperoni = input("Do you want to add pepperoni to your pizza? (Y/N):?").upper()
extra_cheese = input("Do you want to add extra cheese? (Y/N):?").upper()

# todo: work out how much they need to pay for the pizza base don their choice
bill = 0
if size == "S":
    bill = bill + 20
    print(f"Your pizza is ${bill}")
elif size == "M":
    bill += 30
    print(f"Your pizza is ${bill}")
elif size == "L":
    bill += 40
    print(f"Your pizza is ${bill}")
else:
    print("You entered invalid input. Please try again.")


# todo: work out how much to add to their bill if they select to add pepperoni

if pepperoni == "Y":
    if size == "S":
        bill += 2
    print(f"Your pizza is ${bill}")
else:
    bill += 4


# todo: work out how much to add to their bill if they select to add extra_cheese
if extra_cheese == "Y":
    bill += 5
print(f"Your pizza is ${bill}.")

exit()
