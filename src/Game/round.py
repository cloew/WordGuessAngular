from words import GetWordsFor
import random

class Round:
    """ Represents a Round of the Game """
    
    def __init__(self, wordLength):
        """ Initialize the Round """
        self.wordLength = wordLength
        self.wordToGuess = self.pickWord()
        self.triesLeft = 11
        
    def pickWord(self):
        """ Pick a word for the Round """
        words = GetWordsFor(self.wordLength)
        return random.choice(words)