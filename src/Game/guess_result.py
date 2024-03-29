import random

MATCH = 'Correct'
WRONG = 'Wrong'
CLOSE = 'Close'
LEFT = 'Left'
RIGHT = 'Right'
UP = 'Up'
DOWN = 'Down'

class GuessResult:
    """ Represents the Result of a Character Guess """
    probabilities = {WRONG: 2,
                     CLOSE: 5,
                     LEFT: 2,
                     RIGHT: 2,
                     UP: 3,
                     DOWN: 3}
    
    def __init__(self, targetChar, guessChar, leftChar=None, rightChar=None):
        """ Initialize the Guess Results """
        self.guessChar = guessChar
        self.result = self.validateCharacter(targetChar, guessChar, leftChar=leftChar, rightChar=rightChar)
        
    def validateCharacter(self, targetChar, guessChar, leftChar=None, rightChar=None):
        """ Validate the characters """
        if self.match(targetChar, guessChar):
            return MATCH
            
        resultOptions = {}
        if self.up(targetChar, guessChar):
            resultOptions[UP] = self.probabilities[UP]
        else:
            resultOptions[DOWN] = self.probabilities[DOWN]
            
        if self.close(targetChar, guessChar):
            resultOptions[CLOSE] = self.probabilities[CLOSE]
        else:
            resultOptions[WRONG] = self.probabilities[WRONG]
            
        if leftChar and self.close(leftChar, guessChar):
            resultOptions[LEFT] = self.probabilities[LEFT]
        
        if rightChar and self.close(rightChar, guessChar):
            resultOptions[RIGHT] = self.probabilities[RIGHT]
            
        return self.pickResultOption(resultOptions)
        
    def pickResultOption(self, resultOptions):
        """ Pick a result option based on their weight of being the result """
        l = []
        for key in resultOptions:
            for x in range(resultOptions[key]):
                l.append(key)
                
        return random.choice(l)
        
    def match(self, target, guess):
        """ Checks if a guess letter matches a target letter """
        return guess == target
        
    def up(self, target, guess):
        """ Checks if a letter in a guess is above the target letter in the alphabet
        Return true if up, false is assumed to be down since this should never be 
        called if there is a match """
        return ord(target) < ord(guess)
        
    def close(self, target, guess):
        """ Check if the guess letter is within 5 letters of the target """
        return ord(target)-5 <= ord(guess) and ord(guess) <= ord(target)+5