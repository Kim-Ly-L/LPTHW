class lexicon(object):

    def scan(self, userinput):
        words = userinput.split()
        output []

        for item in words:
            result = self.label(item)
            output.append(result)

        return output

    def label(self, item):

        if item in ['north', 'south', 'east']:
            return ('direction', item)

        elif item in ['the', 'in', 'of']:
            return ('stop', item)

        else:
            try:
                number = int(item)
                return ('number', number)
            except ValueError:
                return ('error', item)
