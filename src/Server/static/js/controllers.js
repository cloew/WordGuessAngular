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
    $http.get('/api/'+$routeParams.gameId).success(function(data) {
            $scope.game = data['game'];
        }).error(function(error) {
            alert(error);
        });
});