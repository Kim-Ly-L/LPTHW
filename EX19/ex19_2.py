# The function; it's gonna take in all the following arguments:



print "Welcome. We are going to check your partnership potential now."
print "Are you ready for that? If YES, hit RETURN. If NO, press CTRL-C."
raw_input("> ")

print "Will he/she be your curry? And will you be his/her rice?"
print "Let's find out."

print "First of all, how many hours a week do you enjoy together?"
curry_love = int(raw_input("> "))
print "That's wonderful. But how many hours a week do you fight?"
curry_fight = int(raw_input("> "))
print "Interesting. Then, how about you alone: How many hours a week are you willing to spend with your partner?"
rice_calculus = int(raw_input("> "))


print "Thanks for the information. We will now find out more about your partnership."

curry_potenti = curry_love - curry_fight
curry = curry_potenti / 112 *100
rice_potenti = rice_calculus / 112 *100

print curry
print rice_potenti

print "Your partner's curry potential is %d %." % curry
print "Your rice potential is %d %." % rice_potenti
print "Good luck."



# A week has 168 hours.
# If the average is asleep for about 8 hours each day a week...
# ...that makes 112 hours being awake in total.
