# Osmond Fu
# The Goal: Create a function that generates a message that changes based on a given "mood."


def create_mood_message(name, mood="neutral"):
    if mood == "happy":
        return f"Hey {name}, great to see you smiling!"
    elif mood == "sad":
        return f"I hope your day gets better, {name}."
    elif mood == "neutral":
        return f"Sometimes you have average days, {name}."
    else:
        return f"Hi {name}, hope you're having a good day."


# Ask the user for their name and mood
name = input("What is your name? ")
mood = input("How are you feeling today? (happy/sad/neutral) ")

# Call the function and print the result
response_of_mood = create_mood_message(name, mood)
print(response_of_mood)


# Goal create a function that calculates the average of three numbers. Here are the requirements in detail:


def average(num_one, num_two, num_three):
    result = (num_one + num_two + num_three) / 3
    return result


# Ask the user for three numbers
num_one = float(input("Enter the first number: "))
num_two = float(input("Enter the second number: "))
num_three = float(input("Enter the third number: "))

# Call the function and print the result
print("The average is:", average(num_one, num_two, num_three))
