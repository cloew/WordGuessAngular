'use strict';

angular.module('WordGuess', ['ngRoute', 'WordGuessControllers'])
	.config(['$routeProvider',
		function($routeProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/start_game.html',
			controller: 'StartGameController'
		})
		.when('/game/:gameId', {
			templateUrl: 'static/partials/game.html',
			controller: 'GameController'
		})
		.otherwise({
			redirectTo: '/'
		})
		;
	}])
;