'use strict';

var controllers = angular.module('WordGuessControllers', []);

controllers.controller('StartGameController', function ($scope, $http, $location) {
    $scope.startGame = function() {
        $http.post('/api/startgame').success(function(data) {
            $scope.game = data['game'];
            $location.path('/game/'+$scope.game.id);
        }).error(function(error) {
            alert(error);
        });
    };
});

controllers.controller('GameController', function($scope, $http, $routeParams) {
    $http.defaults.headers.put["Content-Type"] = "application/json";
    
    $scope.currentGuess = {'guesses':[]};
    $http.get('/api/'+$routeParams.gameId).success(function(data) {
            $scope.game = data['game'];
        }).error(function(error) {
            alert(error);
        });
    $scope.setGuess = function(guessString) {
        $scope.currentGuess.guesses = guessString.split('');
    };
    
    $scope.guess = function() {
        $http.put('/api/'+$scope.game.id+'/guess', $scope.currentGuess, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.game = data['game'];
            $scope.results = data['results'];
        }).error(function(error) {
            alert(error);
        });
    };
});