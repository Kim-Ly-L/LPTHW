
class Lexicon(object):
    def scan(self, userinput):
        # First split up the input into a list of words
        words = userinput.split()
        output = []

        # go through list, give each word a label
        for item in words:
            result = self.label(item) # return a nice tuple
            output.append(result)
        # from a list of words for each label
        # Return a list of all of these labled words

        return output

    def label(self, item):
        # always self as the first arg in class!
        # label the item and package it up in a tuple
        # AND dealing the unpredictable with the Exception/Error technique
        if item in ['north', 'south', 'east']:
            return ('direction', item)

        elif item in ['go', 'kill', 'eat']:
            return ('verb', item)

        elif item in ['the', 'in', 'of']:
            return ('stop', item)

        elif item in ['bear', 'princess']:
            return ('noun', item)

        else:
            try:
                number = int(item)
                return ('number', number)
            except ValueError:
                return ('error', item)

lexicon = Lexicon()
