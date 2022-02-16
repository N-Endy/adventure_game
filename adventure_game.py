import time
import random

def print_pause(message):
    print(message)
    time.sleep(2)

def intro(weapon, monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {monster} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not effective) dagger.")
    player_choice(weapon, monster)

def player_choice(weapon, monster):
    choice = valid_input("Enter 1 to knock on the door of the house.\n"
                         "Enter 2 to peer into the cave.\n"
                         "What would you like to do?\n"
                         "(Please enter 1 or 2).\n", ["1", "2"])

    if choice == "1":
        house(weapon, monster)
    elif choice == "2":
        cave(weapon, monster)
    else:
        player_choice(weapon, monster)

def valid_input(prompt, options):
    option = input(prompt).lower()
    if option in options:
        return option
    else:
        print_pause(f"Sorry, the option '{option}' is invalid. Try again!")

def house(weapon, monster):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")

    if "Sword of Ogoroth" in weapon:
        fight(weapon, monster)
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        fight(weapon, monster)


def cave(weapon, monster):
    print_pause("You peer cautiously into the cave")

    if "Sword of Ogoroth" in weapon:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        player_choice(weapon, monster)
    else:
        print_pause("It turns out to be only a small cave")
        print_pause("Your eyes catches a glint of metal behind a rock")
        print_pause("You have found the magical sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you")
        weapon.append("Sword of Ogoroth")
    print_pause("You walk back out to the field")
    player_choice(weapon, monster)


def fight(weapon, monster):
    choice = valid_input("Would you like to "
                         "(1) fight or (2) run away?\n", ["1", "2"])

    if choice == "1":
        if "Sword of Ogoroth" in weapon:
            print_pause(f"As the {monster} moves to attack, "
                        "you unshealth your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in "
                        "your hand as you brace yourself for the attack.")
            print_pause(f"But the {monster} takes one look at your shiney "
                        "new toy and runs away!")
            print_pause(f"You have rid the town of the {monster}. "
                        "You are victorious!")
            play_again(weapon, monster)
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {monster}")
            print_pause("You have been defeated!")
            play_again(weapon, monster)
    elif choice == "2":
        field(weapon, monster)
    else:
        fight(weapon, monster)


def field(weapon, monster):
    print_pause("You run back into the field. "
                "Luckily, you don't seem to have been"
                " followed.")
    player_choice(weapon, monster)


def play_again(weapon, monster):
    choice = valid_input("Would you like to play again? "
                         "(y/n)\n", ["y", "n"])

    if choice == "y":
        weapon.clear()
        print_pause("Welcome to the Adventure Game")
        play_game()
    elif choice == "n":
        print_pause("Thank you for playing! See you next time.")
        exit(0)
    else:
        play_again(weapon, monster)

def play_game():
    weapon = []
    monster = random.choice(["Fairie", "Gorgon", "Troll", "Pirate"])

    intro(weapon, monster)


if __name__ == '__main__':
    play_game()