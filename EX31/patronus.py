print "(You continue the dialogue by hitting ENTER or/and answering truthfully..."
print "...please type in SMALL letters.)"
raw_input ("> ")

print "Hello, my name is Professor Quickle."
raw_input("> ")
print "I've been travelling quite a lot during the past 20 years and I have studied the patronus."
raw_input("> ")
print "You might have heard about one of my former students - Remus Lupin."
print "Did you? [Yes] or [No]"

Remus = raw_input("> ")

if Remus == "yes":
    print "Awesome."
elif Remus == "no":
    print "Oh what a shame. He used to be one of Harry Potter's teachers and supporters during the great war."
else:
    print "Well, he used to be one of Harry Potter's teachers and supporters during the great war."

print "As you might know a patronus incorporates what might be the dearest thing to you."
print "It is your happiest memory, a moment that defines your personality."
raw_input("> ")
print "Powerful wizards have studied methods to summon their patronus."
print "Some of them use the Ridiculus as a substitute for real Dementors."
raw_input("> ")
print "I, however, have worked on a magic mirror that reflects your aura and statements."
print "It then creates a sketch of your personality and your patronus."
print "Let's start!"
raw_input("> ")

print "*Magic mirror appears*"
print "Hello. I will now ask you questions. Please answer truthfully."
raw_input("> ")

print "Laughter or love?"
one = raw_input("> ")

if one == "laughter":
    print "Stones, leaves or sand?"
    sls = raw_input("> ")
    if sls == "stones":
        print "Netflix or Amazon Prime?"
        na = raw_input("> ")
        if na == "netfix":
            print "Your patronus is a mountain goat."
        elif na == "amazon prime":
            print "Your patronus is a turtle."
    elif sls == "leaves":
        print "South America or South Asia?"
        sa = raw_input("> ")

        if sa == "south america":
            print "Your patronus is a mockingjay."
        elif sa == "south asia":
            print "Your patronus is a monkey."

    elif sls == "sand":
        print "Moon or sun?"
        ms = raw_input("> ")

        if ms == "moon":
            print "Your patronus is a scorpion."
        elif ms == "sun":
            print "Your patronus is a camel."

elif one == "love":
    print "Listening, speaking or observing?"
    lso = raw_input("> ")

    if lso == "listening":
        print "Beer or wine?"
        bw = raw_input("> ")

        if bw == "beer":
            print "Your patronus is a Orang Utan."
        elif bw == "wine":
            print "Your patronus is a horse."

    elif lso == "speaking":
        print "Singing or dancing?"
        sd = raw_input("> ")

        if sd == "singing":
            print "Your patronus is a bee swarm."
        elif sd == "dancing":
            print "Your patronus is a rabbit."

    elif lso == "observing":
        print "Cookies or pudding?"
        cm = raw_input("> ")

        if cm == "cookies":
            print "Your patronus is a fox."
        elif cm == "pudding":
            print "Your patronus is a sloth."
