# sets variable (formatter) and value ("%r %r %r %r")
formatter = "%r %r %r %r"

# prints formatter with defineded values/terms; 5,6,7
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# prints formatter without defined values
print formatter % (formatter, formatter, formatter, formatter)
# prints formatter with defined values/strings
# strings will be printed in one line because of commas
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
