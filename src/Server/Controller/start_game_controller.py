from Server.games import StartNewGame
from kao_flask.controllers.json_controller import JSONController

class StartGameController(JSONController):
    """ Controller to handle starting a new Game via JSON """
    
    def performWithJSON(self, json=None):
        return StartNewGame()