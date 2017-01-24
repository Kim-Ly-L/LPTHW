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
decision = Scene("Welcome, Wanderer of the Internet.", "decision",
"""
You can choose between the following two games:
Gothons of Planet Percal #25
or
Save the Paris Agreement
""",
"""
Type in the name of the game you want to play. Pay attention to the upper and lower case.
"""
)

gothon = Scene("Gothons Of Planet Percal", "gothon",
"""
Welcome to this amazing Adventure.
Are You ready to begin the Journey?
""",
"""
Answer with yes or no.
"""
)

central_corridor = Scene("Central Corridor", "central_corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member (oh noes!) and your
last mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're now running down the central corridor to the Weapons Armory when a
Gothon hops out in an evil clown costume filled with hate. He's blocking the door
to the Armory and about to pull a weapon to blast you.
""",
"""
Gothons are aggressive creatures. However, their weakness is their sense of
humour. Researchers have found out that Gothons sympathize with people and
 creatures who make them laugh.
"""
)

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr.
The Gothon bursts into laughter and rolls around on the ground. While its
laughing you run up and use your copy of Nietzsche's notebooks (translated into Gothon)
to lecture the Gothon on the shaky foundations of its ideologies. While it tries
to cope with its existential crisis, you leap through the Weapon Armory door.

You dive roll into the Weapon Armory, crouch and scan the room for more Gothons
that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the neutron bomb in its
container. There's a keypad lock on the box and you need the code to get the bomb
out. If you get the code wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 3 digits.
""",
"""
You better find out the code. After all, you have 10 attempts!
"""
)

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.

You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of fear that they will set off
the bomb under your arm.
""",
"""
Stay calm and remember your goal. You wanted to place the bomb, right?
 Be careful to do it slowly so the Gothons do not panic and shoot at you.
"""
)

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they
can't get out. Now that the bomb is placed you run to the escape pod.

You rush through the ship desperately trying to make it to the escape pod. It seems
like there's no Gothons around, so you run as fast as possible. Eventually you reach
the room with the escape pods, and you now need to pick one to take. Some of them could
be damaged, but you don't have time to look. There's 5 pods, which one do you take?
""",
"""
Enter a number. Hint: Even numbers are regarded as lucky numbers.
"""
)

the_end_winner = Scene("You Made it!", "the_end_winner",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it! YOU WON! Good job!
""",
"""
No help needed. You are a hero!
"""
)

the_end_loser = Scene("Game Over", "the_end_loser",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""",
"""
Bad luck, huh? Try again!
"""
)

generic_death = Scene("Death...", "generic_death", "I have a small puppy that's better at this.",
"""
No need to be desparate! My puppy also had to try a couple of times!
"""
)

vision = Scene("29th of November 2016.", "vision",
"""
You have fallen asleep on your couch while watching Before The Flood. Suddenly,
a bright light appears that wakes you up. You rub your eyes and realize: It is Gandhi!
Gandhi: \"Hello, young fellow. It is time for you to realize that we are at the
edge of something important. Donald Trump has become president and might fulfill
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
*Gandhi disappears*

The next day you come up with the idea of raising awareness first. Fortunately,
you know a super-hacker called XEROX who can broadcast you on the TV News Channel
CNN! XEROX promises you to broadcast you during peak-time.
Therefore, he gives you a remote with which you are supposed to connect your camera
with the channel. When it's finally time to go on TV the remote refuses to obey.
It wants you to type in a three-digit number before it connects you to the channel!
However, XEROX forgot to give you the code. You only have 10 tries to guess the code!
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
You have learned that sometimes it is wiser to cooperate with your opponents
in order to convince them rather than to fight against them.

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
generic_death.add_paths({
    'try again': gothon,
    '*': generic_death
})

game_over.add_paths({
    'try again': vision,
    '*': game_over
})

the_end_loser.add_paths({
    'try again': escape_pod,
    '*': the_end_loser
})

the_end_winner.add_paths({
    '*': the_end_winner
})

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod,
    '*': the_bridge
})

laser_weapon_armory.add_paths({
    '132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory,
    '*': central_corridor
})

gothon.add_paths({
    'yes': central_corridor,
    'begin': central_corridor,
    'ready': central_corridor,
    '*': gothon
})

enlightenment.add_paths({
    '*': enlightenment
})

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

decision.add_paths({
    'Gothons of Planet Percal #25': gothon,
    'Save the Paris Agreement': vision
})

#Make some useful variables to be used in the web application
SCENES = {
    gothon.urlname: gothon,
    central_corridor.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death,
    vision.urlname: vision,
    raise_awareness.urlname : raise_awareness,
    working_class.urlname : working_class,
    enemy_cooperation.urlname : enemy_cooperation,
    last_challenge.urlname : last_challenge,
    enlightenment.urlname : enlightenment,
    game_over.urlname : game_over,
    decision.urlname: decision
}
START = decision
