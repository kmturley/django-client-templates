/**
 * Plate
 * @class Plate
 * @example var plate = new Plate();
 **/

/*globals window, document, plate*/

(function () {
    'use strict';
    
    var module = {
        /**
         * @method init
         */
        init: function () {
            var me = this,
                i = 0;
            this.list = this.checkElements();
            
            // wait one second then load dynamic data
            window.setTimeout(function () {
                me.get(window.location.href, function (data) {
                    for (i = 0; i < me.list.length; i += 1) {
                        console.log('list', i, me.list[i], data);
                        me.update(me.list[i], data);
                    }
                });
            }, 1000);
        },
        /**
         * @method checkElements
         */
        checkElements: function () {
            var i = 0,
                list = [],
                attr = '',
                el = null,
                tmpl = '',
                divs = document.getElementsByTagName('div');
            for (i = 0; i < divs.length; i += 1) {
                attr = divs[i].getAttribute('data-tmpl');
                if (attr) {
                    el = document.getElementById(attr);
                    if (el) {
                        tmpl = new plate.Template(el.text);
                        list.push({tmpl: tmpl, el: divs[i]});
                    }
                }
            }
            return list;
        },
        /**
         * @method update
         */
        update: function (item, data) {
            item.tmpl.render(data, function (err, data) {
                item.el.innerHTML = data;
            });
        },
        /**
         * @method get
         */
        get: function (url, callback) {
            console.log('get', url);
            var me = this;
            if (this.request) {
                this.request.abort();
            } else {
                this.request = new XMLHttpRequest();
            }
            this.request.open('GET', url, true);
            this.request.setRequestHeader('Accept', 'application/json');
            this.request.onload = function () {
                callback(JSON.parse(me.request.response));
            };
            this.request.send();
        }
    };
    module.init();
}());