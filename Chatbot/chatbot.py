
class Chatter(object):
    def __init__(self):
        self.emotion = None

    def start(self, startemo):
        self.emotion = startemo
        print "Hello, what would you like to talk about?"

        userinput = raw_input("> ")

        while userinput != "quit":
            if "angry" in userinput:
                self.emotion = Angry()
            elif "hello" in userinput:
                self.emotion = Welcoming()
            elif "silly" in userinput:
                self.emotion = Coy()


        print self.emotion.respond(userinput)
        userinput = raw_input(self.emotion.ifeel() + "> ")

class Emotion(object):
    def __init__(self, feeling):
        self.feeling = feeling

    def ifeel(self):
        return "I feel %s" % self.feeling

class Angry(Emotion):
    def __init__(self):
        super(Angry, self).__init__("angry")

    def respond(self, userinput):
        if "good" in userinput:
            return "I don't care if you're good or not."
        elif "bad" in userprint:
            return "Good, I'm glad things are bad."
        elif "hello" in userinput:
            return "Go away!"
        else:
            return "What do you want?"

class Welcoming(Emotion):
    def __init__(self):
        super(Welcoming, self).__init__("welcoming")

    def respond(self, userinput):
        if "good" in userinput:
            return "Wonderful."
        elif "bad" in userprint:
            return "Oh no, do you want to talk about it?"
        elif "hello" in userinput:
            return "Hiiii!"
        else:
            return "Excuse me?"


class Coy(Emotion):
    def __init__(self):
        super(Coy, self).__init__("silly")

    def respond(self, userinput):
        if "good" in userinput:
            return "Let me guess, you just had sex."
        elif "bad" in userprint:
            return "Well, you look bad, too."
        elif "hello" in userinput:
            return "...from the other siiiiide."
        else:
            return "I don't understand your language."


app = Chatter()
startemotion = Welcoming()
app.start(startemotion)    #or app.start(Welcoming())
