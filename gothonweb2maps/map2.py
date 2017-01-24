class Scene(object):
    def __init__(self, title, urlname, description, helping):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.helping = helping
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game

vision = Scene("29th of November 2016.", "vision",
"""
You have fallen asleep on your couch while watching Before The Flood. Suddenly,
a bright light appears that wakes you up. You rub your eyes and realize: It is Gandhi!
Gandhi: \"Hello, young fellow. It is time for you to realize that we are at the
edge of something important.Donald Trump has become president and might fulfill
his promise to step out of the Paris Agreement. You what that means for the animals,
the people and our planet, right? It is time to take action.
Are you ready to protect the Paris Agreement?\"
""",
"""
Answer with yes or no.
"""
)

raise_awareness = Scene("First: Raising Awareness.", "raise_awareness",
"""
*Gandhi dissapears*

The next day you come up with the idea of raising awareness first. Fortunately,
you know a super-hacker called XEROX who can broadcast you on the TV News Channel
CNN! XEROX promises you to broadcast you during peak-time.
Therefore, he gives you a remote with which you are supposed to connect your camera
with the channel. When it's finally time to go on TV the remote refuses to obey.
It wants you to type in a three-digit number before it connects you to the channel!
However, XEROX forgot to give you the code. You have only 10 tries to guess the code!
You notice a small handwritten question on the back of the remote:
\"On which day and month was the US-election held?\"
...maybe it's a hint?
""",
"""
Think of the date (month/day) of the US-election 2016.
"""
)

working_class = Scene("The Working Class", "working_class",
"""
After seeing your live-broadcast about the Paris Agreement, your city council decides
to organize a public meeting. However, a lot of middle-class people turn up, too.
They are angry at you opposing Trump and scream at your face.
What will you do now?
""",
"""
Anger is no solution. Listening and understanding disarm conflicts. Explanations do the same.
"""
)

enemy_cooperation = Scene("Invitation to Washington", "enemy_cooperation",
"""
Trump has seen you convincing his supporters. He gets suspicious and invites you
to Washington the next day to have a talk. Two days later you sit in front of him.
What will you do?
""",
"""
Again, anger is no solution. Listening and understanding disarm conflicts. Explanations do the same.
"""
)

last_challenge = Scene("The last Callenge", "last_challenge",
"""
You have learned that sometimes it is wiser to cooperate with your opponents...
...rather than to fight against them.

One month later you are speaking to a crowd of people in front of a huge building.
After finishing your speak you go back to your office that has three exits.
Suddenly, you receive a call from a strange number.
Radical Stranger: \"Hello. I have placed two bombs at your doors. We'll see whether
you can escape or not. Good luck.\"
'What-?!'
You now have to choose between the three doors. Which one do you take?
""",
"""
Enter a number. Hint: Even numbers are regarded as lucky numbers.
"""
)

enlightenment = Scene("Well Done.", "enlightenment",
"""
'Uh... Where am I-?'
*Gandhi suddenly appears*
Gandhi: \"I am very proud of you. You managed to defend the values you believe in.
The question is: Was that all real now? Or only a dream?\"
*Gandhi's body dissolves*
BEEEEEEEEEEEEEEPPPPP----
'What the-?!'
You wake up on your couch, quite dizzy.Your cellphone's alarm is ringing. When you take
a look at the display you realize that it's 6 am in the morning - on the 30th of November!
""",
"""
It is time to achieve change in the real world.
"""
)

game_over = Scene("Game Over", "game_over",
"""
Seems like you made the wrong decision. Don't give up. Remember your dreams and
visions and try again.
""",
"""
No need to be desparate! All idols have failed a couple of times before achieving change.
"""
)

# Define the action commands available in each scene
last_challenge.add_paths({
    '2': enlightenment,
    '*': enlightenment
})

enemy_cooperation.add_paths({
    'listen': last_challenge,
    'understand': last_challenge,
    'explain': last_challenge,
    '*': game_over
})

working_class.add_paths({
    'listen': enemy_cooperation,
    'understand': enemy_cooperation,
    'explain': enemy_cooperation,
    '*': game_over
})

raise_awareness.add_paths({
    '118': working_class,
    '*': game_over
})

vision.add_paths({
    'yes': raise_awareness,
    '*': vision
})

#Make some useful variables to be used in the web application
SCENES = {
    vision.urlname: vision,
    raise_awareness.urlname : raise_awareness,
    working_class.urlname : working_class,
    enemy_cooperation.urlname : enemy_cooperation,
    last_challenge.urlname : last_challenge,
    enlightenment.urlname : enlightenment,
    game_over.urlname : game_over
}
START = vision
