from sys import exit

def happy_ending():
    print "The dagger turns out to be made of Valyrian steel! Lucky you!"
    print "The white walker vanishes after being stabbed by you."
    print "Suddenly, a shining gate appears!"
    print "Now count up to 5."

    count = [1,2,3,4,5]
    for number in count:
        print "%d." % number

    print "WOOOOOSH."
    exit(0)



def white_walker_room():
    print "Your enter the last room."
    print "There is a white walker sitting on a dead but somehow lively horse."
    print "His gaze slowly moves into your direction. You recognize him: He's from Game of Thrones!"
    print "What will you do now? Remember the things you have taken with you from the other rooms."
    print "And: You also have your magic book \"Google\" with you - for the worst case."
    action = raw_input("> ")

    if "dagger" in action:
        happy_ending()
    else:
        dead("The white walker kills you with his spear.")


def pale_man_room():
    print "You enter the next room."
    print "A long table set with huge amounts of tempting, delicious-looking food is in front of you."
    print "A giant pale creature, called the Pale Man, sits at the other end of the table. Its eyes lay on a plate in front of him."
    print "There is a steel dagger behind the creature."
    print "But then again, you could also have the juicy grapes in front of you."
    print "What will you do?"
    do = raw_input("> ")

    if "take" in do or "dagger" in do:
        print "Good choice!"
        white_walker_room()
    elif "grapes" in do or "eat" in do:
        dead("The Pale Man awakes and puts his eyes on his hands, which he holds in front of his face. He sees you and eats your head.")
    else:
        dead("Before taking any action you faint and die. At least nobody ate you.")




def smaug_room():
    print "You enter the next room."
    print "Some bright light blinds your eyes so that you have to close them."
    print "It's the reflection of gold!!! On top of the mass of gold sits a huge dragon, sleeping."
    print "There is a steel dagger between all the gold that you take in order to feel more save."
    print "However, the gold coins look tempting, too... you decide to take some to buy a beer after returning to the real world."
    print "How many do you take?"
    gold = raw_input("> ")

    while type(gold) is not int:
        try:
            gold = int(gold)
        except ValueError:
            print "That wasn't a number. Now quickly decide before the dragon awakes!"
            gold = raw_input("> ")

    if gold < 10:
        print "Good, now run for you life!"
        white_walker_room()
    else:
        print "You have too much! The coins fall out of your pocket which causes a loud sound."
        print "Smaug: \"Raaaaaahwrrr...\""
        dead("Smaug eats you.")



def gollum_room():
    print "You enter the next room."
    print "A small naked creature mutters quietly and crawls into your direction."
    print "Gollum: \"M-myyy.... precious...\""
    print "Gollum: \"An intruder! Shall we eat it?\""
    print "Gollum wants to eat you. What will you suggest to Gollum to distract him and run away?"
    suggestion = raw_input("> ")

    if "riddle" in suggestion or "play" in suggestion:
        print "You win against Gollum. As part of the bet, he/it allows you to pass."
        smaug_room()
    else:
        dead("Gollum gets angry and decides to eat you. By the way, you smell like fish which probably attracts him.")


def dementor_room():
    print "You enter the next room."
    print "A floating creature dressed in a black old shawl appears."
    print "You suddenly feel cold and hopeless - it's a Dementor!"
    print "Remember the spell against Dementors you've learnt in \"Harry Potter\"."
    print "Now remember your happiest memory - and shout it out loud!!!"
    spell = raw_input("> ")

    if spell == "expecto patronum":
        print "Your patronus - an otter - drives off the Dementor."
        pale_man_room()
    else:
        dead("The dementor eats your soul.")

def dead(why):
    print why, "Game over."
    exit(0)

def start():
    print "*mysterious voice appears*"
    print "Welcome, Wanderer."
    print "I know that you've spent a lot of time in the film world."
    print "You surely miss the real world a lot."
    print "Some of us call this world the \"Netflix Nirvana\". Others the \"Amazon Prime Addiction\"."
    print "Whatever name you want to call it - there is only one way to get back to the real world."
    print "Are you courageous enough to challenge the \"Castle of Movie Monsters\"?"
    print "If YES hit return. If NO press CTRL-C."
    raw_input("> ")

    print "Good, then let the games begin."
    print "Please type in your answers in small letters."
    print "In case you don't know what to do: Remember that you carry the magic book called \"Google\" with you."
    print "Understood?"
    raw_input("> ")

    print "*two doors appear*"
    print "Do you take the left door or the right door?"
    choice = raw_input("> ")

    if choice == "left":
        dementor_room()
    elif choice == "right":
        gollum_room()
    else:
        dead("You can't decide, huh? Seems like you'll stay in this film world forever.")

start()
