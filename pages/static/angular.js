/**
 * Angular
 * @class Angular
 * @example var angular = new Angular();
 **/

/*globals window, document, angular*/

var app = angular.module('app', [])

    .controller('dynamic', function ($scope, $http, $templateCache) {
        $http.get(window.location.href).success(function (data) {
            $scope.items = data.items;
        });
    });