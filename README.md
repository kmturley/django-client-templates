# Django Client Templates

Example showing two examples of how to render django templates client side. Sharing the same template code between the front and backend!

* Plate - Uses a Django raw_include tag + PlateJS to re-render templates in the browser
* Angular - Uses django-angular module + AngularJS directive to re-render templates in the browser

## Installation

Ensure you have Python and Django installed using the instructions at:
https://docs.djangoproject.com/en/1.8/intro/install/

## Usage

Run the command:

    python manage.py migrate
    python manage.py runserver
    
## Plate input

    {% load pages_tags %}
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Django Client Templates - PlateJS</title>
        <meta name="description" content="" />
        <meta name=viewport content="width=device-width,initial-scale=1" />
    </head>
    <body>
        <h1>PlateJS</h1>
        <div class="row" data-tmpl="nav">
            {% include "plate/includes/nav.html" %}
        </div>
        <div class="row" data-tmpl="list">
            {% include "plate/includes/list.html" %}
        </div>
        <script type="text/template" id="list">
            {% raw_include "plate/includes/list.html" %}
        </script>
        <script type="text/template" id="nav">
            {% raw_include "plate/includes/nav.html" %}
        </script>
        <script src="/static/libs/plate/plate.min.js"></script>
        <script src="/static/plate.js"></script>
    </body>
    </html>

## Plate output

    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Django Client Templates - PlateJS</title>
        <meta name="description" content="" />
        <meta name=viewport content="width=device-width,initial-scale=1" />
    </head>
    <body>
        <h1>PlateJS</h1>
        <div class="row" data-tmpl="nav">
            <ul class="nav">
                <li><a href="#">Static data 1</a></li>
                <li><a href="#">Static data 2</a></li>
                <li><a href="#">Static data 3</a></li>
            </ul>
        </div>
        <div class="row" data-tmpl="list">
            <div class="list">
                    <div class="item">
                        <h1>Static data 1</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1</p>
                    </div>
                    <div class="item">
                        <h1>Static data 2</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2</p>
                    </div>
                    <div class="item">
                        <h1>Static data 3</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3</p>
                    </div>
            </div>
        </div>
        <script type="text/template" id="list">
            <div class="list">
                {% for item in items %}
                    <div class="item">
                        <h1>{{ item.name }}</h1>
                        <p>{{ item.desc }}</p>
                    </div>
                {% endfor %}
            </div>
        </script>
        <script type="text/template" id="nav">
            <ul class="nav">
                {% for item in items %}
                    <li><a href="#">{{ item.name }}</a></li>
                {% endfor %}
            </ul>
        </script>
        <script src="/static/libs/plate/plate.min.js"></script>
        <script src="/static/plate.js"></script>
    </body>
    </html>
    
## Angular input

    {% load pages_tags %}
    <!doctype html>
    <html lang="en" ng-app="app">
    <head>
        <meta charset="utf-8" />
        <title>Django Client Templates - AngularJS</title>
        <meta name="description" content="" />
        <meta name=viewport content="width=device-width,initial-scale=1" />
    </head>
    <body>
        <h1>AngularJS</h1>
        <div class="row" template="nav">
            {% include "angular/includes/nav.html" with ng=0 %}
        </div>
        <div class="row" template="list">
            {% include "angular/includes/list.html" with ng=0 %}
        </div>
        <script type="text/ng-template" id="nav">
            {% include "angular/includes/nav.html" with ng=1 %}
        </script>
        <script type="text/ng-template" id="list">
            {% include "angular/includes/list.html" with ng=1 %}
        </script>
        <script src="/static/libs/angular/angular.min.js"></script>
        <script src="/static/angular.js"></script>
    </body>
    </html>

## Angular output

    <!doctype html>
    <html lang="en" ng-app="app">
    <head>
        <meta charset="utf-8" />
        <title>Django Client Templates - AngularJS</title>
        <meta name="description" content="" />
        <meta name=viewport content="width=device-width,initial-scale=1" />
    </head>
    <body>
        <h1>AngularJS</h1>
        <div class="row" template="nav">
            <ul class="nav">
                    <li><a href="#">Static data 1</a></li>
                    <li><a href="#">Static data 2</a></li>
                    <li><a href="#">Static data 3</a></li>
            </ul>
        </div>
        <div class="row" template="list">
            <div class="list">
                    <div class="item">
                        <h1>Static data 1</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1</p>
                    </div>
                    <div class="item">
                        <h1>Static data 2</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2</p>
                    </div>
                    <div class="item">
                        <h1>Static data 3</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3</p>
                    </div>
            </div>
        </div>
        <script type="text/ng-template" id="nav">
            <ul class="nav" ng-repeat="item in items">
                <li><a href="#" ng-bind="item.name">Static data 1</a></li>
                <li><a href="#" ng-bind="item.name">Static data 2</a></li>
                <li><a href="#" ng-bind="item.name">Static data 3</a></li>
            </ul>
        </script>
        <script type="text/ng-template" id="list">
            <div class="list" ng-repeat="item in items">
                    <div class="item">
                        <h1 ng-bind="item.name">Static data 1</h1>
                        <p ng-bind="item.desc">Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1</p>
                    </div>
                    <div class="item">
                        <h1 ng-bind="item.name">Static data 2</h1>
                        <p ng-bind="item.desc">Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2</p>
                    </div>
                    <div class="item">
                        <h1 ng-bind="item.name">Static data 3</h1>
                        <p ng-bind="item.desc">Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3</p>
                    </div>
            </div>
        </script>
        <script src="/static/libs/angular/angular.min.js"></script>
        <script src="/static/angular.js"></script>
    </body>
    </html>