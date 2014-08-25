'use strict';

angular.module('WordGuess', ['ngRoute', 'WordGuessControllers'])
	.config(['$routeProvider',
		function($routeProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/start_game.html',
			controller: 'StartGameController'
		})
		.when('/about', {
			templateUrl: 'static/partials/about.html',
			controller: 'AboutController'
		})
		.otherwise({
			redirectTo: '/'
		})
		;
	}])
;