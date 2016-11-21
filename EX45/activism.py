#-*-coding:utf-8-*-
from sys import exit
from random import randint
from ex43 import Scene


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('enlightenment')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Gameover(Scene):

    quips = [
        "You're not ready yet.",
        "Your intuition was wrong.",
        "Try to think about what Nelson Mandela would have done in your position.",
        "You're not the chosen one. Find somebody else you can follow and support.",
        "Don't give up."
    ]

    def enter(self):
        print Gameover.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Vision(Scene):

    def enter(self):
        print "29th of November 2016. You have fallen asleep on your couch while watching 'Before The Flood'."
        print "Suddenly, a bright light appears that wakes you up."
        print "You rub your eyes and realize: It is Gandhi!"
        print "Gandhi: \"Hello, young fellow.\""
        print "Gandhi: \"It is time for you to realize that we are at the edge of something important.\""
        print "Gandhi: \"Donald Trump has become president and might fulfill his promise to step out of the Paris Agreement.\""
        print "Gandhi: \"You what that means for the animals, the people and our planet, right?\""
        raw_input("> ")

        print "Gandhi: \"It is time to take action.\""
        print "Gandhi: \"Are you ready to protect the Paris Agreement?\""
        answer = raw_input("> ")

        if answer == "no":
            print "Gandhi: \"You must be courageous. If it's not you, who else will do it?\""
        elif answer == "yes":
            print "Gandhi: \"Good.\""
        else:
            print "Gandhi: \"I don't understand what you mean.\""

        print "*Gandhi dissapears*"
        return 'raise_awareness'


class RaiseAwareness(Scene):

    def enter(self):
        print "The next day you come up with the idea of raising awareness first."
        print "Fortunately, you know a super-hacker called XEROX who can broadcast you on the TV News Channel CNN!"
        print "XEROX promises you to broadcast you during peak-time."
        print "Therefore, he gives you a remote with which you are supposed to connect your camera with the channel."
        print "When it's finally time to go on TV the remote refuses to obey."
        print "It wants you to type in a three-digit number before it connects you to the channel!"
        print "However, XEROX forgot to give you the code. You have only 10 tries to guess the code!"
        print "You notice a small handwritten question on the back of the remote:"
        print "\"On which day and month was the US-election held?\""
        print "...maybe it's a hint?"
        code = "118"
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            guesses += 1
            print "BZZZED!"
            print "Guesses left: ", 10 - guesses
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "LUCKY YOU. You found out the right code and are now able to speak to millions of German citizens!"
            return 'working_class'
        else:
            print "OH NO. You didn't manage to find out the code."
            return 'gameover'

class WorkingClass(Scene):

    def enter(self):
        print "After seeing your live-broadcast about the Paris Agreement, your city council decides to organize a public meeting."
        print "However, a lot of middle-class people turn up, too."
        print "They are angry at you opposing Trump and scream at your face."
        print "What will you do now?"
        action = raw_input("> ")

        if "scream" in action or "insult" in action or "kill" in action or "shout" in action or "beat" in action or "ignore" in action:
            print "That's no solution. Think about the reason why Trump has become president-elect in first place."
            print "It is time to listen to the needs of all classes so populists won't be able to grow stronger."
            return 'gameover'
        elif "comfort" in action or "explain" in action or "listen" in action or "understand" in action:
            print "A good choice! Peace can only begin with a shared understanding."
            print "If one side is not willing to listen to the other, it will become almost impossible to solve a conflict."
            print "This rule also applies to the elite, academics, who do not regard the working class as equals."
            print "As long as one party feels superior to the other, there will be always a dispute."
            return 'trump_cooperation'
        else:
            print "You can't do this. Think about a better way to solve this."
            print "Meanwhile I will explain the situation again."
            return 'working_class'

class TrumpCooperation(Scene):

    def enter(self):
        print "Trump has seen you convincing his supporters."
        print "He gets suspicious and invites you to Washington the next day to have a talk."
        print "Two days later you sit in front of him."
        print "What will you do?"
        action = raw_input("> ")

        if "insult" in action or "kill" in action or "blackmail" in action or "hate" in action or "scream" in action:
            print "That's no solution! You can't defeat the evil with evil actions!"
            return 'gameover'
        elif "explain" in action or "talk" in action or "speak" in action or "convince" in action or "convinced" in action:
            print "Trump is listening to you."
            print "He tries to understand your arguments as he claims to be pragmatic."
            print "His hair is raising as he's trying. He kind of reminds you of a solarium-addicted Super Sayajin."
            print "You can see that he starts to realize the importance of the Paris Agreement."
            print "Trump: \"Tremendous potential, this agreement... tremendous.\""
            print "He promises you to think about his future steps before making a final decision."
            print "After all, it was only for the sake of campaigning that he proposed all his ridiculous plans."
            print "You have learned that sometimes it is wiser to cooperate with your opponents..."
            print "...rather than to fight against them."
            raw_input("> ")
            return 'paris_agreement'
        else:
            print "You can't do this. Come up with a better idea!"
            print "Meanwhile I will explain the situation again."
            return 'trump_cooperation'

class ParisAgreement(Scene):

    def enter(self):
        print "-" * 10
        print "One month later you are speaking to a crowd of people in front of a huge building."
        print "After finishing your speak you go back to your office that has three exits."
        print "Suddenly, you receive a call from a strange number."
        print "Radical Stranger: \"Hello. I have placed two bombs at your doors.\""
        print "Radical Stranger: \"We'll see whether you can escape or not. Good luck.\""
        print "BEEP."
        print "'What-?!'"
        print "You now have to choose between the three doors. Which one do you take?"
        escape = randint(1,3)
        guess = raw_input("Door No.> ")

        while type(guess) is not int:
            try:
                guess = int(guess)
            except ValueError:
                print "That wasn't a number. Now quickly decide!"
                guess = raw_input("Door No.> ")

        if guess != escape:
            print "Right after you open the door the bomb blows up and kills you."
            print "BOOOOM"
            return 'enlightenment'
        else:
            print "Lucky you! You took the right door which allows you to escape."
            print "Nevertheless, the adrenaline was too much for you to cope with after all the stressful days."
            print "You faint."
            return 'enlightenment'

class Enlightenment(Scene):

    def enter(self):
        raw_input("> ")
        print "Uh-"
        raw_input("> ")
        print "'Where am I-?'"
        print "*Gandhi suddenly appears*"
        print "Gandhi: \"I am very proud of you.\""
        print "Gandhi: \"You managed to defend the values you believe in.\""
        print "Gandhi: \"The question is: Was that all real now? Or only a dream?\""
        print "*Gandhi's body dissolves*"
        print "BEEEEEEEEEEEEEEPPPPP----"
        raw_input("> ")
        print "'What the-?!'"
        print "You wake up on your couch, quite dizzy."
        print "Your cellphone's alarm is ringing."
        print "When you take a look at the display you realize that it's 6 am in the morning - on the 30th of November!"
        print "-" * 10

class Map(object):

    scenes = {
        'vision': Vision(),
        'raise_awareness': RaiseAwareness(),
        'working_class': WorkingClass(),
        'trump_cooperation': TrumpCooperation(),
        'paris_agreement': ParisAgreement(),
        'enlightenment': Enlightenment(),
        'gameover': Gameover()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene('vision')

the_map = Map('vision')
the_game = Engine(the_map)
the_game.play()
