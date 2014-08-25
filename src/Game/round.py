from guess_results import GuessResults
from words import GetWordsFor
import random

class Round:
    """ Represents a Round of the Game """
    
    def __init__(self, wordLength):
        """ Initialize the Round """
        self.wordLength = wordLength
        self.wordToGuess = self.pickWord()
        self.triesLeft = 11
        self.completed = False
        
    def pickWord(self):
        """ Pick a word for the Round """
        words = GetWordsFor(self.wordLength)
        return random.choice(words)
        
    def guess(self, guesses):
        """ Return the results of the list of guesses """
        results = GuessResults(self.wordToGuess, guesses)
        if results.isCorrectGuess():
            self.completed = True
        else:
            self.triesLeft -= 1
        return results