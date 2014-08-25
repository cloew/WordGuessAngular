from Server.Controller.start_game_controller import StartGameController
from Server.Controller.guess_controller import GuessController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          Endpoint('/api/startgame', post=StartGameController()),
          Endpoint('/api/<int:gameId>/guess', put=GuessController())]