from guess_result import GuessResult, MATCH

class GuessResults:
    """ Represents the Results of a Guess """
    
    def __init__(self, word, guesses):
        """ Initialize the Guess Results """
        self.results = []
        for i in range(len(word)):
            leftChar = None
            if i > 0:
                leftChar = word[i-1]
                
            rightChar = None
            if i < (len(word)-1):
                rightChar = word[i+1]
                
            result = GuessResult(word[i], guesses[i], leftChar=leftChar, rightChar=rightChar)
            self.results.append(result)
        
    def isCorrectGuess(self):
        """ Returns if the entire guess was correct """
        return len([result for result in self.results if result == MATCH]) > 0