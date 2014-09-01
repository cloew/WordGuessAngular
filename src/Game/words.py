
words = {2:['at',
            'be',
            'to'],
         3:['two'],
         4:['four'],
         5:['three'],
         6:['beggar']}

sortedKeys = words.keys()
sortedKeys.sort()
STARTING_LENGTH = sortedKeys[0]
ENDING_LENGTH = sortedKeys[len(sortedKeys)-1]
         
def GetWordsFor(wordLength):
    """ Return the list of words for the appropriate length """
    return words[wordLength]
    
def GetStartingLength():
    """ Returns the Length for the first round of a game """
    return STARTING_LENGTH
    
def HasNextLength(wordLength):
    """ Return if there is a round that can be played after the given word length """
    return wordLength < ENDING_LENGTH
    
def GetNextLength(wordLength):
    """ Return the length of the word for the next round """
    return wordLength + 1
