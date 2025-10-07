# Notes - Introduction
# 16 September
# Osmond Fu

# Create an algorithim to solve a problem
# Problem: Create our own chatbot
#   MeGPT

# 1.Greet the user with a predetermined statement
greeting = "Hello! I am a chatbot"

# 1a. Print the greeting
print(greeting)

# 2a. Introduce the bot
print("My name is MeGPT")
print("I'm not like the other guy")
print("I am completetly deterministic")

# 3. Wow the user with some maths
print("I bet you don't know what 8x8 is.")
print("I can do it.")
print(f"8x8 is actually {8 + 8}.")

print("what is pi squared?")
print("I'm smart, I can do it too.")
print(f"it is {3.14159265359**2}.")


# 4. Make the b ot crash oout a little bit.
print("The quick brown fox jums over the lazy dog." * 1)

# 5. Get the name of the user. state it and use it
username = input("what is your name?")
print(f"It's nice to meet you, {username}!")

# 6. Ask the first question
question1 = input("Whats your favourite food?")
print(f"{question1} is Delicious!")

# 7. Ask the second question
question2 = input("Where are you from?")
print(f"{question2} is a beautiful place!")

# 8. Ask the third question
question3 = input("How old are you?")
print(f"I am {question3} + 1000 years older!")

# 9. Say goodbye using the user's name
print(f"Goodbye, {username}! It was nice talking to you.")

# 10. See if the user is someone specific
# 10a. If they're someone speicfic tell them a secret

if username == "osmond":
    print("I know you like burgers.")
    print("You can see all the secret Information.")
