# work-mcdobot.py
# A simple McDonald's bot that asks if you want fries with your meal

# Ask the user
answer = input("Would you like fries with your meal? (Yes/No)")

# Clean up the input using string methods
answer = answer.strip().lower()  # removes spaces and makes lowercase

# Respond based on cleaned input
if answer == "yes":
    print("Great! Fries coming right up ")
elif answer == "no":
    print("No problem! Maybe next time.")
else:
    print(f'I heard "{answer.title()}", but I don’t understand.')
