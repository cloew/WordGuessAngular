'use strict';

var controllers = angular.module('WordGuessControllers', []);

controllers.controller('StartGameController', function ($scope) {
    $scope.startGame = function() {
        alert("Starting Game");
    };
});

controllers.controller('AboutController', function() {
});