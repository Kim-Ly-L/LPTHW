import urllib

class Scene(object):
    def __init__(self, title, urlname, description, imgurl):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.imgurl = imgurl
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game

gothon = Scene("Gothons Of Planet Percal #25", "gothon",
"""
Welcome to this amazing Adventure.
Are You ready to begin the Journey?
""", imgurl=urllib.urlopen('http://giphy.com/gifs/ufo-spaceship-abduction-3o85xuG8NPw9Okvquc'))

central_corridor = Scene("Central Corridor", "central_corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member (oh noes!) and your
last mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're now running down the central corridor to the Weapons Armory when a
Gothon hops out in an evil clown costume filled with hate. He's blocking the door
to the Armory and about to pull a weapon to blast you.
""", imgurl=urllib.urlopen('http://giphy.com/gifs/loop-tumblr-featured-10thPb0Ycbqfqo'))

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
""", imgurl=urllib.urlopen('http://giphy.com/gifs/season-17-the-simpsons-17x13-3o6MbdTboTFWOUsLkc'))

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.

You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of fear that they will set off
the bomb under your arm.
""", imgurl=urllib.urlopen('http://giphy.com/gifs/rap-eminem-dope-kwqq0OhgJWWR2'))

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
""", imgurl=urllib.urlopen('http://giphy.com/gifs/comedy-bang-scott-aukerman-cbbtv-PBg4KWciMK6zu'))

the_end_winner = Scene("You Made it!", "the_end_winner",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it! YOU WON! Good job!
""", imgurl=urllib.urlopen('http://giphy.com/gifs/breaking-bad-bryan-cranston-i-won-xT0GqssRweIhlz209i'))

the_end_loser = Scene("Game Over", "the_end_loser",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""", imgurl=urllib.urlopen('http://giphy.com/gifs/wip-short-loser-3oz8xD8KWiVO4obzby'))

generic_death = Scene("Death...", "death", "I have a small puppy that's better at this.",
imgurl=urllib.urlopen('http://giphy.com/gifs/the-simpsons-2x10-3o6Mb5WxERQyuy7qJa'))

# Define the action commands available in each scene
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

#Make some useful variables to be used in the web application
SCENES = {
    gothon.urlname: gothon,
    central_corridor.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death
}

#IMAGEURL = {
#    gothon.imgurl : 'http://giphy.com/gifs/ufo-spaceship-abduction-3o85xuG8NPw9Okvquc',
#    central_corridor.imgurl : 'http://giphy.com/gifs/loop-tumblr-featured-10thPb0Ycbqfqo',
#    laser_weapon_armory.imgurl : 'http://giphy.com/gifs/season-17-the-simpsons-17x13-3o6MbdTboTFWOUsLkc',
#    the_bridge.imgurl : 'http://giphy.com/gifs/rap-eminem-dope-kwqq0OhgJWWR2',
#    escape_pod.imgurl : 'http://giphy.com/gifs/comedy-bang-scott-aukerman-cbbtv-PBg4KWciMK6zu',
#    the_end_winner.imgurl : 'http://giphy.com/gifs/breaking-bad-bryan-cranston-i-won-xT0GqssRweIhlz209i',
#    the_end_loser.imgurl : 'http://giphy.com/gifs/wip-short-loser-3oz8xD8KWiVO4obzby',
#    generic_death.imgurl : 'http://giphy.com/gifs/the-simpsons-2x10-3o6Mb5WxERQyuy7qJa'
#}

START = gothon
