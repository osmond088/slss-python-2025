# Osmond Fu

# Adventure 1


# Introduce


name = input("Hello, Whats your name?")
print(f"Nice to meet you {name}")
print("you're a regular high school student")
print("You open up a stall that has a portal opened")

# Choice 1

choice1 = input("Do you enter or walk away (enter/walk) ")

if choice1 == "walk":
    print("You have walked away")
    print("You wonder what would have happened")
    print("Normal Life ending!")

elif choice1 == "enter":
    print("the portal takes you deep into an abyss")
    print("Eery whispers start playing")
    print("You land on a rock")

# Choice 2

choice2 = input("A sword is nearby do you pick it up? (pick/leave)")

if choice2 == "pick":
    sword = True
    print("You picked up a rusty sword | Attack +1!")
    print("You're now ready to defend yourself!")
else:
    sword = False
    print("You walk past the sword.| Defense 0")


# Monster

print("you venture deeper into the hallway")
if sword:
    print("A monster leaps out and attacks you!")
choicemonster = input(" Do you run away or attack back? (attack/escape) ")

if choicemonster == "escape":
    print("You tried to run away and the monster caught up!")
    print("You Lost!")
else:
    sword = True
    print("You go in for an attack! ")
choiceattack = input("GO for the head or the legs (head/body)")
if choiceattack == "head":
    print("The monster evades and eats you! You lost")
if choiceattack == "body":
    monsterdead = True
    print("You caught the monster offguard! The monster is slayn!")
if choicemonster == "attack":
    sword = False
    print("You dont have a sword! You died.")

# going deeper
