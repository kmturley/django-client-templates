/**
 * Example
 * @class Example
 * @example var example = new Example();
 **/

/*globals window, document, plate*/

(function () {
    'use strict';

    var el = document.getElementById('list'),
        tmpl = document.getElementById('tmpl-list'),
        template = new plate.Template(tmpl.text),
        json = {
            "people": [
                {"name": "New data 1"},
                {"name": "New data 2"},
                {"name": "New data 3"}
            ]
        };

    template.render(json, function (err, data) {
        el.innerHTML = data;
    });
}());



