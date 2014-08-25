'use strict';

var controllers = angular.module('WordGuessControllers', []);

controllers.controller('StartGameController', function ($scope) {
    $scope.someMethod = function() {
        alert("Build Something");
    };
});

controllers.controller('AboutController', function() {
});