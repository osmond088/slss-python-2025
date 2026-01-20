# Notes - Adventure Game
# 25 September
# Osmond Fu

import time

# 1. Get the player's name
name = input("What is your name? ")

# 2. Greet the player with story introduction
print(f"Hi, {name}. You are a normal high school student,")
time.sleep(2)
print("but one afternoon you hear strange whispers coming from the basement.")
time.sleep(2)
print("You discover a glowing, swirling portal hidden behind an old locker.")
time.sleep(2)
print("The air feels heavy, as if calling you inside.")
time.sleep(2)

# 3. First choice
choice1 = input("Do you ENTER the portal or WALK away? (enter/walk) ")

if choice1 == "walk":
    print("You step back. The portal flickers, then vanishes forever.")
    time.sleep(2)
    print("You return home, but you always wonder what adventure you missed.")
    time.sleep(2)
    print("Ending: Normal Life ")

elif choice1 == "enter":
    print("The portal pulls you in! You land hard on cold stone.")
    time.sleep(2)
    print("You are inside a dark dungeon. Torches flicker on the walls.")
    time.sleep(2)
    print("A foul smell fills the air. Danger is close...")
    time.sleep(2)

    # 4. Second choice
    choice2 = input(
        "On the ground is a rusty sword. Do you PICK it up or LEAVE it? (pick/leave) "
    )

    if choice2 == "pick":
        has_sword = True
        print("You grip the sword. Even though it’s old, it makes you feel braver.")
        time.sleep(2)
    else:
        has_sword = False
        print("You ignore the sword and continue unarmed. A risky choice...")
        time.sleep(2)

    # 5. Third choice
    choice3 = input(
        "Two paths lie ahead: LEFT (dark tunnel with whispers) or RIGHT (glowing chamber). (left/right) "
    )

    if choice3 == "left":
        print("You step into the tunnel. The whispers grow louder...")
        time.sleep(2)
        print("Suddenly, a monstrous beast leaps from the shadows!")
        time.sleep(2)

        if has_sword:
            print("You raise your sword as the monster charges!")
            time.sleep(2)
            print("After a fierce battle, you strike the final blow. The beast falls.")
            time.sleep(2)

            # 6. New choice after monster
            choice5 = input(
                "Victorious, you see a deeper passage. Do you SEARCH the dungeon or EXIT now? (search/exit) "
            )

            if choice5 == "search":
                print("You venture deeper. The dungeon trembles around you.")
                time.sleep(2)
                print(
                    "At the end of the passage, you find a chamber filled with gold and jewels!"
                )
                time.sleep(2)
                print(
                    "You grab what you can and discover a hidden exit back to the school."
                )
                time.sleep(2)
                print("Ending: Treasure Hunter 💰")
            elif choice5 == "exit":
                print("You leave through a side tunnel and escape into daylight.")
                time.sleep(2)
                print("Your bravery will be remembered forever.")
                time.sleep(2)
                print("Ending: Hero’s Victory 🏆")
            else:
                print("You hesitate too long. The dungeon collapses around you.")
                time.sleep(2)
                print("Ending: Game Over 💀")
        else:
            print("You try to run, but the monster is too fast.")
            time.sleep(2)
            print("With no weapon, you are defeated instantly.")
            time.sleep(2)
            print("Ending: Game Over 💀")

    elif choice3 == "right":
        print("You enter the glowing chamber. The air hums with strange magic.")
        time.sleep(2)
        print("In the middle is a large treasure chest, glowing faintly.")
        time.sleep(2)

        choice4 = input("Do you OPEN the chest or LEAVE it alone? (open/leave) ")

        if choice4 == "open":
            print("You open the chest... but it’s a trap!")
            time.sleep(2)
            print("Poison gas bursts out, filling the room.")
            time.sleep(2)
            print("You collapse instantly.")
            time.sleep(2)
            print("Ending: Game Over 💀")
        elif choice4 == "leave":
            print("You resist temptation and leave the chest untouched.")
            time.sleep(2)
            print("Behind it, you find a hidden doorway leading back to the school.")
            time.sleep(2)
            print("You survived the dungeon’s tricks!")
            time.sleep(2)
            print("Ending: Cautious Victory ✅")
        else:
            print("You freeze in indecision. The chamber begins to collapse!")
            time.sleep(2)
            print("Ending: Game Over 💀")

else:
    print("You stand frozen. The portal flickers, then disappears.")
    time.sleep(2)
    print("The adventure passes you by...")
    time.sleep(2)
    print("Ending: Missed Adventure ⌛")
