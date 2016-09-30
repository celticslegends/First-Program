# This is the first program I have made from scratch! It is very simple and not
# extremely intricate, but it works!
from sys import exit
# def is very important in this excfercise.
def open_door():
    print "There are cannibals hiding in this house."
    print "Because of the situation, they are killing humans and harvesting/eating"
    print "them. Will you: \"fight\", \"burn the house\", or \"reason with them\"?"
    # This below code allows you to make choices below and continues the prompt
    # as the game progresses. You can keep adding layers and layers to it if you
    # choose.
    choice = raw_input("> ")
    # I've noticed that you can use either: if "" in choice:, or: if choice ==
    # "":    either one of these allows you to input the raw input and take the
    # game further.
    if "fight" in choice:
        basement()
    elif "burn the house" in choice:
        print "The house fire is seen from miles away and you end up drawing in"
        print "U.N troops who capture you and throw you in a FEMA camp."
        exit(0)
    elif "reason with them" in choice:
        print "You cannot reason with cannibals. They over power you and eat you."
        exit(0)
    else:
        print "You end up in their slaughterhouse! Not good!"
# def allows you to make a new section of the game and input new aspects to it.
def basement():
    print "After over powering them and outgunning them with your Glock 19 and"
    print "limited ammunition, the basement leads to a secret passageway and bunker"
    print "that has 1 years supply of food and also provides a secret door that"
    print "allows you to enter/exit the location undetected and plan what to do next."
    exit(0)

def unchecked_power():
    print "You come in contact with resistance groups that try and stop the"
    print "U.N from unchecked power. As a group, you have decided that surrender"
                                # it is good that you are addign prompts so you
                                # can choose which input to type in.
    print "is not an option. Your choices are: \"search for weapons and ammo\", \"head"
    print "out west\", or \"find a larger food source\"."

    choice = raw_input("> ")

    if "search for weapons and ammo" in choice:
        print "You locate a bunker that provides you with enough defensive and"
        print "offensive artillery that you venture up to the mountains to stand"
        print "your ground and win the fight!"
        exit(0)
    elif "head out west" in choice:
        print "This decision ends up being a gift and a curse. A lot of people"
        print "die from starvation, but because of the remote territory and lack"
        print "of foreign troops, you end up building several outposts and trade"
        print "locations to restart civilization. It is not for the faint of heart."
        exit(0)
    elif "find a larger food source" in choice:
        print "Instead of fighting the U.N, or heading out west, you lack the food"
        print "source availability due to winter and a majority of your group dies."
        exit(0)


def wander_woods():
    print "U.N troops and other entities are roaming the area and placing survivors"
    print "in FEMA camps. Will you: \"surrender\", or \"evade them\"?"
    # this one portion below was the only setback when first making this game.
    # you forget to add in: choice = raw_input("> ") and you kept receiving an
    # error message. It is usually a small error that can throw off everything.
    choice = raw_input("> ")

    if "surrender" in choice:
        print "You stay in a concentration camp the rest of your life."
        exit(0)
    elif "evade them" in choice:
        unchecked_power()
    else:
        print "You kill a U.N soldier, wear his gear and steal a vehicle to escape"
        print "from the area."
        exit(0)

def secluded_fire():
    print "Because of the large troop presence and the fact that you stopped being"
    print "resourceful and sat around, you are rounded up by the U.N forces."
    print "Next time be more evasive and tactical!"
    # adding in this exit(0) allows the game to end and start over when you place
    # it below a def.
    exit(0)

def start():
    print "There has been an EMP attack on America and all the power is out."
    print "After severe fighting and food shortages, to escape from the hoardes"
    print "of people, you have come across what looks like an abandoned home in the woods."
    print "Will you: \"open the door\", \"wander in the woods\", or \"find a secluded area\"?"

    choice = raw_input("> ")

    if choice == "open the door":
        open_door()
    elif choice == "wander in the woods":
        wander_woods()
    elif choice == "find a secluded area":
        secluded_fire()
    else:
        print "You run out of food and water and end up eaten by wolves!"

# without this little piece of code below, the whole game will not work. It is
# the small things that matter!
start()
