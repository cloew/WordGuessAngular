from Server.game_wrapper import GameWrapper
from kao_flask.controllers.json_controller import JSONController

class GuessController(JSONController):
    """ Controller to allow a player to guess the word for the current Round """
    
    def performWithJSON(self, gameId):
        wrapper = GameWrapper(id=gameId)
        game = wrapper.game
        results = game.guess(self.json['guesses'])
        
        resultJSON = wrapper.toJSON()
        resultJSON['results'] = results.results
        return resultJSON