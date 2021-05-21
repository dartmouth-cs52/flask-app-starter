# Flask App Starter Pack

This is a quick starter pack for a flask app, setup to run on Heroku.

## Installation Instructions

1. Clone the repository
2. `python3 -m venv ./venv`
3. `source ./venv/bin/activate`
4. `pip3 install -r requirements.txt`
5. `flask run` to start the server

## Overview of Routes

The `src/routers/example_router.py` file is an example router with a few routes set up.

1. `GET /healthcheck` automatically returns a successful response
2. `GET /example` will return back a JSON representation of the query parameters
3. `POST /example` will return back a JSON representation of the request body
4. `GET /error` will return a 500 error code (as an example)

## Changing Routes

You can modify route method and name by editing the `@app.route` function. The first parameter is the route name and the second is its supported methods (e.g. `GET`, `POST`, `PUT`, `DELETE`).

The function immediately beneath a call to `@app.route` is the function that will be called when a request is sent to that route. If the route name supports multiple methods, you can determine which one was called with `request.method`. As shown in the example, you can get query parameters via `request.args` and you can get a request body via `request.data`. In the example, we convert the body into a Python dictionary using the `json.loads` function.

The `format_success` and `format_error` functions make it easy to send back specific payloads. If you want to send an error response, return a ternary with the second parameter being the response code. See the `GET /error` route for an example.

## Adding Additional Routers

You can add additional routers by adding to the `src/routers` directory. Make sure to update `src/routers/__init__.py` to include a new line importing your router: `from . import [name of your router file]`.

## Deploying to Heroku

This starterpack is set up to run on Heroku. Create a new app on the Heroku Dashboard and add the `heroku/python` buildpack. Connect to your repository and you should be good to go!
