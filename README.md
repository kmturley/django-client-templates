# Django Client Templates

Example showing how to render django templates client side. Sharing the same template code between the two!

## Installation

Ensure you have Python and Django installed using the instructions at:
https://docs.djangoproject.com/en/1.8/intro/install/

## Usage

Run the command:

    python manage.py migrate
    python manage.py runserver

## Output

    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Django Client Templates</title>
        <meta name="description" content="" />
        <meta name=viewport content="width=device-width,initial-scale=1" />
    </head>
    <body>
        <div id="list">
            <ul>
                <li>John Doe</a></li>
                <li>Sally Taylor</a></li>
                <li>David Smith</a></li>
            </ul>
        </div>
        <script type="text/template" id="tmpl-list">
            <ul>
                {% for person in people %}
                    <li>{{ person.name }}</a></li>
                {% endfor %}
            </ul>
        </script>
        <script src="/static/libs/plate.min.js"></script>
        <script src="/static/example.js"></script>
    </body>
    </html>