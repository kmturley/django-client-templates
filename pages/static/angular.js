/**
 * Angular
 * @class Angular
 * @example var angular = new Angular();
 **/

/*globals window, document, angular*/

var app = angular.module('app', [])

    /**
     * @method template
     */
    .directive('template', function ($http, $templateCache, $compile) {
        return ({
            restrict: 'A',
            link: function (scope, el, attrs) {
                window.setTimeout(function () {
                    $http.get(window.location.href).success(function (data) {
                        scope.items = data.items;
                        el.html($templateCache.get(attrs.template));
                        $compile(el.contents())(scope);
                    });
                }, 1000);
            }
        });
    });