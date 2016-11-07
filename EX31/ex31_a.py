print "Welcome to this mysterious Castle of Mystery."
print "You're goal in the game is to find your way out."
print "Let's begin."
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your arms off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

    print "Do you want to continue exploring the castle? If YES hit return."
    print "If NO hit CTRL-C."

    Continue = raw_input("> ")

    print "There are two stairs. One goes up and the other goes to the basement."
    print "Do you want to go #up or #down?"

    stairs = raw_input("> ")

    if stairs == "up":
        print "You're in a small tower and suddenly, you feel helpless."
        print "You jump out of the window and commit suicide."
    elif stairs == "down":
        print "You're in a basement now. There's a small window that could be opened by force."
        print "Do you want to #open it or do you want to #wait?"

        window = raw_input("> ")

        if window == "open":
            print "You're free! Eventually wounded, but at least you found the way out!"
        elif window == "wait":
            print "A serial killer suddenly shows up and kills you. Too bad."
        else:
            print "A serial killer suddenly shows up and kills you. Too bad."
    else:
        print "A serial killer suddenly shows up and kills you. Too bad."

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
        print "There's a hole on the ground and there's an access to an air system on the ceiling."
        print "You can now decide whether you want to crawl into the hole or climb up into the air system."
        print "Do you want to #crawl or #climb?"

        escape = raw_input("> ")

        if escape == "crawl":
            print "You're lucky! The hole turns out to be a tunnel! You managed to find the way out! Congrats!"
        elif escape == "climb":
            print "Oh no! You got trapped in the air system and now die a slowly death."
        else:
            print "A serial killer suddenly shows up and kills you. Too bad."

    else:
        print "The insanity rots your eyes into a pool of muck. Game over."

else:
    print "You stumble around and fall on a knife and die. Good job!"
